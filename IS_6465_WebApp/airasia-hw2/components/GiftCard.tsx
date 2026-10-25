import Image from "next/image";
import Link from "next/link";
import { Card, CardContent } from "@/components/ui/card";
import type { GiftCardData } from "@/lib/gift-cards";

export default function GiftCard({
  id,
  title,
  value,
  points,
  image,
}: GiftCardData) {
  return (
    <Link
      href={`/card-details/${id}`}
      className="block h-full rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-rose-600"
    >
      <Card className="h-full w-full rounded-2xl border-2 border-gray-300 bg-white p-6 transition-all duration-200 hover:-translate-y-1 hover:border-rose-500 hover:shadow-lg">
        <CardContent className="flex flex-col gap-6 p-0">
          {/* Gift Card Image */}
          <div className="flex aspect-[1.55] items-center justify-center rounded-lg border-2 border-gray-300 bg-gray-100">
            <Image
              src={image}
              alt={`${title} image`}
              width={120}
              height={120}
            />
          </div>

          {/* Gift Card Title */}
          <h2 className="text-xl font-bold text-rose-600 underline">{title}</h2>

          {/* Gift Card Value */}
          <p className="text-lg text-gray-500">
            ${value.toLocaleString()} value
          </p>

          {/* Points Required */}
          <div>
            <p className="text-gray-500">Points required</p>
            <p className="text-2xl font-bold text-gray-900">
              {points.toLocaleString()} points
            </p>
          </div>
        </CardContent>
      </Card>
    </Link>
  );
}
