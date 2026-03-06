    SELECT 'SubscriptionStatus' AS Dim, SubscriptionStatus AS Value, COUNT(*) AS Cnt
    FROM group6.Subscription
    GROUP BY SubscriptionStatus

UNION ALL
    SELECT 'PriceModel', PriceModel, COUNT(*)
    FROM group6.Ad
    GROUP BY PriceModel

UNION ALL
    SELECT 'PlacementType', PlacementType, COUNT(*)
    FROM group6.Ad_Slot
    GROUP BY PlacementType

UNION ALL
    SELECT 'EventType', EventType, COUNT(*)
    FROM group6.Ad_Interaction
    GROUP BY EventType
ORDER BY Dim, Value;