WITH ClickEvents AS (
    SELECT
        i.DeliveryID,
        i.SlotSeqNo,
        i.EventSeqNo,
        i.EventAt,
        s.AdID,
        a.PriceModel,
        a.BidAmount,
        s.PricePaid,
        -- useful for joining up the business hierarchy
        c.CampaignID,
        c.CampaignName,
        adv.AdvertiserID,
        adv.AdvertiserName
    FROM group6.Ad_Interaction i
    JOIN group6.Ad_Slot s
      ON s.DeliveryID = i.DeliveryID AND s.SlotSeqNo = i.SlotSeqNo
    JOIN group6.Ad a
      ON a.AdID = s.AdID
    JOIN group6.Campaign c
      ON c.CampaignID = a.CampaignID
    JOIN group6.Advertiser adv
      ON adv.AdvertiserID = c.AdvertiserID
    WHERE i.EventType = 'Click'
)
SELECT
    DeliveryID,
    SlotSeqNo,
    EventSeqNo,
    EventAt,
    AdvertiserName,
    CampaignName,
    AdID,
    PriceModel,

    -- "Revenue from this click"
    RevenueFromClick =
        CASE
            WHEN PriceModel = 'CPC' THEN BidAmount
            -- For CPM / CPV, a click isn't how those models bill.
            -- You can either show 0, or allocate a share of the slot's PricePaid to each click.
            ELSE 0.00
        END,

    -- OPTIONAL: allocate the realized slot spend across clicks in that same slot
    -- (If a slot has 2 clicks and PricePaid=1.00, each click gets 0.50 allocated)
    AllocatedSlotSpendPerClick =
        CASE
            WHEN PricePaid IS NULL THEN NULL
            ELSE CAST(PricePaid AS decimal(10,2))
                 / NULLIF(SUM(1) OVER (PARTITION BY DeliveryID, SlotSeqNo), 0)
        END,

    -- rollups (window functions) so the table is immediately informative
    ClicksOnThisAd = COUNT(*) OVER (PARTITION BY AdID),
    TotalCPCRevenueForAd =
        SUM(CASE WHEN PriceModel = 'CPC' THEN BidAmount ELSE 0 END) OVER (PARTITION BY AdID)

FROM ClickEvents
ORDER BY EventAt, DeliveryID, SlotSeqNo, EventSeqNo;