CREATE SCHEMA group6;
GO

DROP TABLE IF EXISTS group6.User;
DROP TABLE IF EXISTS group6.Subscription;
DROP TABLE IF EXISTS group6.Plan;
DROP TABLE IF EXISTS group6.Advertiser;
DROP TABLE IF EXISTS group6.Campaign;
DROP TABLE IF EXISTS group6.Ad;
DROP TABLE IF EXISTS group6.Ad_Slot;
DROP TABLE IF EXISTS group6.Ad_Interaction;
DROP TABLE IF EXISTS group6.Billing;

CREATE TABLE group6.User
(
    UserID VARCHAR(210) NOT NULL,
    Email VARCHAR(210) NOT NULL,
    FirstName VARCHAR(210) NOT NULL,
    LastName VARCHAR(210) NOT NULL,
    CONSTRAINT User_PK PRIMARY KEY (UserID)
);

CREATE TABLE group6.Plan
(
    PlanID INT,
    PlanName VARCHAR(20) NOT NULL,
    BillingPeriod DATE,
    AdFreeFlad BIT,
    Price MONEY,
    Currency VARCHAR(10)
        CONSTRAINT Plan_PK PRIMARY KEY (PlanID),
);

CREATE TABLE group6.Subscription
(
    SubscriptionID INT NOT NULL,
    SubscriptionStatus VARCHAR(20) NOT NULL,
    StartDate DATE,
    EndDate DATE,
    AutoRenewFlag BIT,
    UserID VARCHAR(210),

    CONSTRAINT Subscription_PK PRIMARY KEY (SubscriptionID),
    CONSTRAINT Subscription_FK1 FOREIGN KEY (UserID) REFERENCES group6.User(UserID),
    CONSTRAINT Subscription_FK2 FOREIGN KEY (PlanID) REFERENCES group6.Plan(PlanID)
);

CREATE TABLE group6.Advertiser
(
    AdvertiserID INT NOT NULL,
    AdvertiserName VARCHAR(250) NOT NULL,
    CONSTRAINT Advertiser_PK PRIMARY KEY (AdvertiserID)
);

CREATE TABLE group6.Campaign
(
    CampaignID INT NOT NULL,
    CampaignName VARCHAR(250) NOT NULL,
    StartDate DATE,
    EndDate DATE,
    Budget MONEY,
    AdvertiserID INT,
    CONSTRAINT Campaign_PK PRIMARY KEY (CampaignID),
    CONSTRAINT Campaign_FK FOREIGN KEY (AdvertiserID) REFERENCES group6.Advertiser(AdvertiserID)
);

CREATE TABLE group6.Ad
(
    AdID INT NOT NULL,
    AdType VARCHAR(30),
    DurationSec TIME,
    PriceModel MONEY,
    BidAmount MONEY,
    ClickURL VARCHAR(250),
    CampaignID INT,
    CONSTRAINT Ad_PK PRIMARY KEY (AdID),
    CONSTRAINT Ad_FK FOREIGN KEY (CampaignID) REFERENCES group6.Campaign(CampaignID)
);

CREATE TABLE group6.Ad_Slot
(
    SlotSeqNo INT NOT NULL,
    PlacementType VARCHAR(30),
    RequestedAt DATE,
    DeliveryID INT NOT NULL,
    AdID INT,
    ServedAt DATE,
    PricePaid MONEY,
    CONSTRAINT Ad_Slot_PK PRIMARY KEY (SlotSeqNo, DeliveryID, AdID),
    CONSTRAINT Ad_Slot_FK FOREIGN KEY (AdID) REFERENCES group6.Ad(AdID)
);

CREATE TABLE group6.Ad_Interaction
(
    DeliveryID INT,
    EventSeqNo INT NOT NULL,
    EventDate DATE,
    EventType VARCHAR(30),
    CONSTRAINT Ad_Interaction_PK PRIMARY KEY (DeliveryID, EventSeqNo),
    CONSTRAINT Ad_Interaction_FK FOREIGN KEY (DeliveryID) REFERENCES group6.Ad_Slot(DeliveryID)
);

CREATE TABLE group6.Billing
(
    SubscriptionID INT,
    TxnSeqNo INT NOT NULL,
    TxnType VARCHAR(30),
    TxnDate DATE NOT NULL,
    Amount MONEY,
    TxnStatus BIT,
    CONSTRAINT Billing_PK PRIMARY KEY (SubscriptionID, TxnSeqNo),
    CONSTRAINT Billing_FK FOREIGN KEY (SubscriptionID) REFERENCES group6.Subscription(SubscriptionID)
);