import Link from "next/link";
import { buttonVariants } from "@/components/ui/button";
import GiftCard from "@/components/GiftCard";
import { giftCards } from "@/lib/gift-cards";

export default function CardList() {
  return (
    <main className="flex flex-1 flex-col gap-8 bg-zinc-50 p-4 font-sans dark:bg-black">
      <div className="flex items-center justify-between">
        <h1 className="text-4xl font-bold">Gift Cards</h1>

        <Link
          href="/card-add"
          className={buttonVariants({
            variant: "default",
            className: "w-48",
          })}
        >
          Add Gift Card
        </Link>
      </div>

      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {giftCards.map((card) => (
          <GiftCard key={card.id} {...card} />
        ))}
      </div>
    </main>
  );
}
