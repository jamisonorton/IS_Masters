/* =========================================================
   group6 FULL SEED SCRIPT (re-runnable)
   - Clears existing data (child -> parent)
   - Inserts base sample data (>=5 rows per table)
   - Generates realistic Ad_Interaction volume (default 60/served slot)
   - Ensures each served slot has >= 1 Impression
   ========================================================= */

SET NOCOUNT ON;

BEGIN TRAN;

-- =========================
-- 1) Clear existing data (FK-safe order)
-- =========================
DELETE FROM group6.Ad_Interaction;
DELETE FROM group6.Ad_Slot;
DELETE FROM group6.Billing;
DELETE FROM group6.Subscription;
DELETE FROM group6.Ad;
DELETE FROM group6.Campaign;
DELETE FROM group6.Advertiser;
DELETE FROM group6.SubscriptionPlan;
DELETE FROM group6.AppUser;

-- =========================
-- 2) Insert base entities (parents first)
-- =========================

-- AppUser (>=5)
INSERT INTO group6.AppUser
    (UserID, Email, FirstName, LastName)
VALUES
    ('u001', 'ava.martin@example.com', 'Ava', 'Martin'),
    ('u002', 'noah.lee@example.com', 'Noah', 'Lee'),
    ('u003', 'mia.patel@example.com', 'Mia', 'Patel'),
    ('u004', 'liam.garcia@example.com', 'Liam', 'Garcia'),
    ('u005', 'emma.wilson@example.com', 'Emma', 'Wilson');

-- SubscriptionPlan (>=5)
INSERT INTO group6.SubscriptionPlan
    (PlanID, PlanName, BillingPeriod, AdFreeFlag, Price, Currency)
VALUES
    (1, 'Free', 'Monthly', 0, 0.00, 'USD'),
    (2, 'Plus Monthly', 'Monthly', 1, 9.99, 'USD'),
    (3, 'Plus Annual', 'Annual', 1, 99.99, 'USD'),
    (4, 'Basic Monthly', 'Monthly', 0, 4.99, 'USD'),
    (5, 'Family Annual', 'Annual', 1, 149.99, 'USD');

-- Advertiser (>=5)
INSERT INTO group6.Advertiser
    (AdvertiserID, AdvertiserName)
VALUES
    (101, 'Acme Outdoors'),
    (102, 'BrightBank'),
    (103, 'Citrus Mobile'),
    (104, 'Dove & Pine Home'),
    (105, 'Evergreen Fitness');

-- Campaign (>=5)
INSERT INTO group6.Campaign
    (CampaignID, CampaignName, StartDate, EndDate, Budget, AdvertiserID)
VALUES
    (1001, 'Acme Spring Launch', '2026-01-15', '2026-04-15', 25000.00, 101),
    (1002, 'BrightBank Cash Back', '2026-02-01', '2026-06-30', 40000.00, 102),
    (1003, 'Citrus 5G Push', '2026-03-01', NULL, 60000.00, 103),
    (1004, 'Dove & Pine Renovation', '2026-01-10', '2026-03-31', 15000.00, 104),
    (1005, 'Evergreen New Year Fitness', '2025-12-20', '2026-02-28', 30000.00, 105);

-- Ad (>=5)
INSERT INTO group6.Ad
    (AdID, AdType, DurationSec, PriceModel, BidAmount, ClickURL, CampaignID)
VALUES
    (2001, 'Video', 30, 'CPV', 0.08, 'https://example.com/acme', 1001),
    (2002, 'Audio', 15, 'CPM', 3.50, 'https://example.com/brightbank', 1002),
    (2003, 'Banner', 10, 'CPC', 0.75, 'https://example.com/citrus', 1003),
    (2004, 'Video', 45, 'CPV', 0.12, 'https://example.com/dovepine', 1004),
    (2005, 'Audio', 30, 'CPM', 4.25, 'https://example.com/evergreen', 1005);

-- Subscription (>=5)
INSERT INTO group6.Subscription
    (SubscriptionID, SubscriptionStatus, StartDate, EndDate, AutoRenewFlag, UserID, PlanID)
VALUES
    (3001, 'Active'  , '2026-02-10', NULL        , 1, 'u001', 2),
    (3002, 'Canceled', '2026-01-01', '2026-02-15', 0, 'u002', 4),
    (3003, 'Expired' , '2025-12-01', '2026-01-01', 0, 'u003', 3),
    (3004, 'Active'  , '2026-03-01', NULL        , 1, 'u004', 1),
    (3005, 'Active'  , '2026-02-20', NULL        , 1, 'u005', 5);

-- Billing (>=5)
INSERT INTO group6.Billing
    (SubscriptionID, TxnSeqNo, TxnType, TxnDateTime, Amount, TxnStatus)
VALUES
    (3001, 1, 'Charge', '2026-02-10T09:15:00', 9.99, 'Succeeded'),
    (3001, 2, 'Charge', '2026-03-10T09:15:00', 9.99, 'Pending'),
    (3002, 1, 'Charge', '2026-01-01T08:00:00', 4.99, 'Succeeded'),
    (3002, 2, 'Refund', '2026-01-20T12:30:00', 4.99, 'Succeeded'),
    (3005, 1, 'Charge', '2026-02-20T07:45:00', 149.99, 'Failed');

-- Ad_Slot (>=5)  (include one unfilled slot)
INSERT INTO group6.Ad_Slot
    (DeliveryID, SlotSeqNo, PlacementType, RequestedAt, AdID, ServedAt, PricePaid)
VALUES
    (4001, 1, 'PreRoll'      , '2026-03-05T10:00:00', 2001, '2026-03-05T10:00:02', 0.08),
    (4001, 2, 'BetweenSongs' , '2026-03-05T10:04:00', 2002, '2026-03-05T10:04:01', 3.50),
    (4002, 1, 'MidRoll'      , '2026-03-05T11:15:00', 2004, '2026-03-05T11:18:30', 0.12),
    (4003, 1, 'BetweenSongs' , '2026-03-06T09:30:00', 2003, '2026-03-06T09:30:01', 0.75),
    (4004, 1, 'PreRoll'      , '2026-03-06T12:00:00', NULL , NULL                , NULL);

-- =========================
-- 3) Generate realistic Ad_Interaction (50+ per served slot)
-- =========================
DECLARE @EventsPerServedSlot INT = 60;

;WITH
    ServedSlots
    AS
    (
        SELECT
            s.DeliveryID,
            s.SlotSeqNo,
            s.AdID,
            a.PriceModel,
            a.AdType,
            s.ServedAt
        FROM group6.Ad_Slot s
            JOIN group6.Ad a
            ON a.AdID = s.AdID
        WHERE s.AdID IS NOT NULL
            AND s.ServedAt IS NOT NULL
    ),
    Numbers
    AS
    (
        -- integers 1..@EventsPerServedSlot
        SELECT TOP (@EventsPerServedSlot)
            ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
        FROM sys.all_objects
    ),
    BaseEvents
    AS
    (
        SELECT
            ss.DeliveryID,
            ss.SlotSeqNo,
            n.n AS EventSeqNo,
            -- bursty-ish timestamps near ServedAt, then spreading out
            DATEADD(MILLISECOND,
            (ABS(CHECKSUM(NEWID())) % 900) + (n.n - 1) * 250,
            ss.ServedAt
        ) AS EventAt,
            ss.PriceModel,
            ss.AdType
        FROM ServedSlots ss
    CROSS JOIN Numbers n
    ),
    TypedEvents
    AS
    (
        SELECT
            DeliveryID,
            SlotSeqNo,
            EventSeqNo,
            EventAt,
            CASE
            -- Always at least one Impression per served slot
            WHEN EventSeqNo = 1 THEN 'Impression'

            -- One "resolution" event early for audio/video
            WHEN EventSeqNo = 2 AND AdType IN ('Video','Audio')
                THEN CASE WHEN (ABS(CHECKSUM(NEWID())) % 100) < 75 THEN 'Complete' ELSE 'Skip' END

            -- For banners, clicks show up earlier more often
            WHEN EventSeqNo = 2 AND AdType = 'Banner'
                THEN CASE WHEN (ABS(CHECKSUM(NEWID())) % 100) < 40 THEN 'Click' ELSE 'Impression' END

            -- Remaining events: weighted by price model
            ELSE
                CASE
                    WHEN PriceModel = 'CPC' THEN
                        CASE
                            WHEN (ABS(CHECKSUM(NEWID())) % 100) < 12 THEN 'Click'
                            ELSE 'Impression'
                        END

                    WHEN PriceModel = 'CPV' THEN
                        CASE
                            WHEN (ABS(CHECKSUM(NEWID())) % 100) < 3 THEN 'Click'
                            WHEN (ABS(CHECKSUM(NEWID())) % 100) < 12 AND AdType IN ('Video','Audio')
                                THEN CASE WHEN (ABS(CHECKSUM(NEWID())) % 100) < 70 THEN 'Complete' ELSE 'Skip' END
                            ELSE 'Impression'
                        END

                    ELSE -- CPM
                        CASE
                            WHEN (ABS(CHECKSUM(NEWID())) % 100) < 2 THEN 'Click'
                            ELSE 'Impression'
                        END
                END
        END AS EventType
        FROM BaseEvents
    )
INSERT INTO group6.Ad_Interaction
    (DeliveryID, SlotSeqNo, EventSeqNo, EventAt, EventType)
SELECT DeliveryID, SlotSeqNo, EventSeqNo, EventAt, EventType
FROM TypedEvents;

COMMIT;