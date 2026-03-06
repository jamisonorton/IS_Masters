IF SCHEMA_ID('group6') IS NULL
    EXEC('CREATE SCHEMA group6;');
GO

DROP TABLE IF EXISTS group6.Billing;
DROP TABLE IF EXISTS group6.Ad_Interaction;
DROP TABLE IF EXISTS group6.Ad_Slot;
DROP TABLE IF EXISTS group6.Subscription;
DROP TABLE IF EXISTS group6.Ad;
DROP TABLE IF EXISTS group6.Campaign;
DROP TABLE IF EXISTS group6.Advertiser;
DROP TABLE IF EXISTS group6.SubscriptionPlan;
DROP TABLE IF EXISTS group6.AppUser;
GO

CREATE TABLE group6.AppUser
(
    UserID VARCHAR(210) NOT NULL,
    Email VARCHAR(210) NOT NULL,
    FirstName VARCHAR(210) NOT NULL,
    LastName VARCHAR(210) NOT NULL,

    CONSTRAINT AppUser_PK PRIMARY KEY (UserID),
    CONSTRAINT AppUser_Email_UQ UNIQUE (Email)
);
GO

CREATE TABLE group6.SubscriptionPlan
(
    PlanID INT NOT NULL,
    PlanName VARCHAR(50) NOT NULL,
    BillingPeriod VARCHAR(20) NOT NULL,
    AdFreeFlag BIT NOT NULL CONSTRAINT SubscriptionPlan_AdFree_DF DEFAULT (0),
    Price DECIMAL(10,2) NOT NULL CONSTRAINT SubscriptionPlan_Price_DF DEFAULT (0),
    Currency VARCHAR(10) NOT NULL CONSTRAINT SubscriptionPlan_Currency_DF DEFAULT ('USD'),

    CONSTRAINT SubscriptionPlan_PK PRIMARY KEY (PlanID),
    CONSTRAINT SubscriptionPlan_BillingPeriod_CK CHECK (BillingPeriod IN ('Monthly','Annual')),
    CONSTRAINT SubscriptionPlan_Price_CK CHECK (Price >= 0)
);
GO

CREATE TABLE group6.Advertiser
(
    AdvertiserID INT NOT NULL,
    AdvertiserName VARCHAR(250) NOT NULL,

    CONSTRAINT Advertiser_PK PRIMARY KEY (AdvertiserID)
);
GO

CREATE TABLE group6.Campaign
(
    CampaignID INT NOT NULL,
    CampaignName VARCHAR(250) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NULL,
    Budget DECIMAL(12,2) NOT NULL CONSTRAINT Campaign_Budget_CK CHECK (Budget >= 0),
    AdvertiserID INT NOT NULL,

    CONSTRAINT Campaign_PK PRIMARY KEY (CampaignID),
    CONSTRAINT Campaign_Advertiser_FK FOREIGN KEY (AdvertiserID)
        REFERENCES group6.Advertiser(AdvertiserID),
    CONSTRAINT Campaign_Dates_CK CHECK (EndDate IS NULL OR EndDate >= StartDate)
);
GO

CREATE TABLE group6.Ad
(
    AdID INT NOT NULL,
    AdType VARCHAR(30) NOT NULL,
    DurationSec INT NOT NULL CONSTRAINT Ad_Duration_CK CHECK (DurationSec > 0),
    PriceModel VARCHAR(10) NOT NULL,
    BidAmount DECIMAL(10,2) NOT NULL CONSTRAINT Ad_Bid_CK CHECK (BidAmount >= 0),
    ClickURL VARCHAR(250) NULL,
    CampaignID INT NOT NULL,

    CONSTRAINT Ad_PK PRIMARY KEY (AdID),
    CONSTRAINT Ad_Campaign_FK FOREIGN KEY (CampaignID)
        REFERENCES group6.Campaign(CampaignID),
    CONSTRAINT Ad_PriceModel_CK CHECK (PriceModel IN ('CPM','CPC','CPV'))
);
GO

CREATE TABLE group6.Subscription
(
    SubscriptionID INT NOT NULL,
    SubscriptionStatus VARCHAR(20) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NULL,
    AutoRenewFlag BIT NOT NULL CONSTRAINT Subscription_AutoRenew_DF DEFAULT (0),
    UserID VARCHAR(210) NOT NULL,
    PlanID INT NOT NULL,

    CONSTRAINT Subscription_PK PRIMARY KEY (SubscriptionID),
    CONSTRAINT Subscription_AppUser_FK FOREIGN KEY (UserID)
        REFERENCES group6.AppUser(UserID),
    CONSTRAINT Subscription_Plan_FK FOREIGN KEY (PlanID)
        REFERENCES group6.SubscriptionPlan(PlanID),
    CONSTRAINT Subscription_Status_CK CHECK (SubscriptionStatus IN ('Active','Canceled','Expired')),
    CONSTRAINT Subscription_Dates_CK CHECK (EndDate IS NULL OR EndDate >= StartDate)
);
GO

CREATE TABLE group6.Billing
(
    SubscriptionID INT NOT NULL,
    TxnSeqNo INT NOT NULL,
    TxnType VARCHAR(30) NOT NULL,
    TxnDateTime DATETIME2 NOT NULL,
    Amount DECIMAL(10,2) NOT NULL CONSTRAINT Billing_Amount_CK CHECK (Amount >= 0),
    TxnStatus VARCHAR(20) NOT NULL,

    CONSTRAINT Billing_PK PRIMARY KEY (SubscriptionID, TxnSeqNo),
    CONSTRAINT Billing_Subscription_FK FOREIGN KEY (SubscriptionID)
        REFERENCES group6.Subscription(SubscriptionID),
    CONSTRAINT Billing_TxnType_CK CHECK (TxnType IN ('Charge','Refund')),
    CONSTRAINT Billing_TxnStatus_CK CHECK (TxnStatus IN ('Succeeded','Failed','Pending'))
);
GO

CREATE TABLE group6.Ad_Slot
(
    DeliveryID INT NOT NULL,
    SlotSeqNo INT NOT NULL,
    PlacementType VARCHAR(30) NOT NULL,
    RequestedAt DATETIME2 NOT NULL,

    AdID INT NULL,
    ServedAt DATETIME2 NULL,
    PricePaid DECIMAL(10,2) NULL,

    CONSTRAINT Ad_Slot_PK PRIMARY KEY (DeliveryID, SlotSeqNo),
    CONSTRAINT Ad_Slot_Ad_FK FOREIGN KEY (AdID)
        REFERENCES group6.Ad(AdID),
    CONSTRAINT Ad_Slot_Placement_CK CHECK (PlacementType IN ('PreRoll','MidRoll','BetweenSongs')),
    CONSTRAINT Ad_Slot_PricePaid_CK CHECK (PricePaid IS NULL OR PricePaid >= 0),
    CONSTRAINT Ad_Slot_ServedAt_CK CHECK (ServedAt IS NULL OR ServedAt >= RequestedAt)
);
GO

CREATE TABLE group6.Ad_Interaction
(
    DeliveryID INT NOT NULL,
    SlotSeqNo INT NOT NULL,
    EventSeqNo INT NOT NULL,
    EventAt DATETIME2 NOT NULL,
    EventType VARCHAR(30) NOT NULL,
    CONSTRAINT Ad_Interaction_PK PRIMARY KEY (DeliveryID, SlotSeqNo, EventSeqNo),
    CONSTRAINT Ad_Interaction_AdSlot_FK FOREIGN KEY (DeliveryID, SlotSeqNo)
        REFERENCES group6.Ad_Slot(DeliveryID, SlotSeqNo),
    CONSTRAINT Ad_Interaction_EventType_CK CHECK (EventType IN ('Impression','Click','Complete','Skip'))
);
GO