import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";

import { getGiftCardById } from "@/lib/gift-cards";
import { buttonVariants } from "@/components/ui/button";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

type CardDetailsProps = {
  params: Promise<{ id: string }>;
};

export default async function CardDetails({ params }: CardDetailsProps) {
  const { id } = await params;
  const card = getGiftCardById(id);

  if (!card) {
    notFound();
  }

  return (
    <main className="flex flex-1 flex-col gap-6 bg-zinc-50 p-6 font-sans dark:bg-black">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <h1 className="text-4xl font-bold">Gift Card Details</h1>

        <Link
          href={`/card-update/${card.id}`}
          className={buttonVariants({
            variant: "default",
            className: "w-48",
          })}
        >
          Update Gift Card
        </Link>
      </div>

      {/* Back Link */}
      <Link href="/card-list" className="text-sm text-gray-500 hover:underline">
        ← Back to Gift Cards
      </Link>

      {/* Gift Card Details */}
      <Card className="w-full max-w-3xl">
        <CardHeader>
          <CardTitle className="text-2xl">{card.title}</CardTitle>
        </CardHeader>

        <CardContent>
          <div className="grid gap-8 md:grid-cols-2">
            {/* Gift Card Image */}
            <div className="flex aspect-square items-center justify-center rounded-lg border bg-gray-100 p-6">
              <Image
                src={card.image ?? "/window.svg"}
                alt={card.title}
                width={250}
                height={250}
                className="object-contain"
              />
            </div>

            {/* Gift Card Information */}
            <div className="flex flex-col gap-6">
              <div>
                <p className="text-sm text-gray-500">Card Name</p>
                <p className="text-xl font-semibold">{card.title}</p>
              </div>

              <div>
                <p className="text-sm text-gray-500">Card Type</p>
                <p className="text-lg font-medium">{card.type}</p>
              </div>

              <div>
                <p className="text-sm text-gray-500">Card Value</p>
                <p className="text-lg font-medium">
                  ${card.value.toLocaleString()}
                </p>
              </div>

              <div>
                <p className="text-sm text-gray-500">Points Required</p>
                <p className="text-2xl font-bold">
                  {card.points.toLocaleString()} points
                </p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </main>
  );
}
