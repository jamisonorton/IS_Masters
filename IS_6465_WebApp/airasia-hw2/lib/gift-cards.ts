export type GiftCardData = {
  id: string;
  title: string;
  type: string;
  value: number;
  points: number;
  image: string;
};

export const giftCards: GiftCardData[] = [
  {
    id: "1",
    title: "AirAsia e-Gift Card",
    type: "Electronic",
    value: 25,
    points: 2500,
    image: "/airasia-logo.png",
  },
  {
    id: "2",
    title: "Coffee House Gift Card",
    type: "Electronic",
    value: 50,
    points: 5000,
    image: "/globe.svg",
  },
  {
    id: "3",
    title: "AirAsia Premium Gift Card",
    type: "Physical",
    value: 100,
    points: 10000,
    image: "/window.svg",
  },
];

export function getGiftCardById(id: string) {
  return giftCards.find((card) => card.id === id);
}
