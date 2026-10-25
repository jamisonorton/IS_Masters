import { notFound } from "next/navigation";
import { getGiftCardById } from "@/lib/gift-cards";
import Link from "next/link";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
  CardFooter,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

type CardUpdateProps = {
  params: Promise<{ id: string }>;
};

export default async function CardUpdate({ params }: CardUpdateProps) {
  const { id } = await params;
  const card = getGiftCardById(id);

  if (!card) {
    notFound();
  }

  return (
    <main className="flex flex-1 flex-col gap-6 bg-zinc-50 p-6 dark:bg-black">
      <h1 className="text-4xl font-bold">Update Gift Card</h1>

      <Card className="w-full max-w-xl">
        <CardHeader>
          <CardTitle>{card.title}</CardTitle>
          <CardDescription>
            Update the gift card information below.
          </CardDescription>
        </CardHeader>

        <CardContent>
          <form id="update-card-form" action="/card-list" method="GET">
            <div className="flex flex-col gap-6">
              {/* Card Name */}
              <div className="grid gap-2">
                <Label htmlFor="title">Card Name</Label>
                <Input
                  id="title"
                  name="title"
                  type="text"
                  defaultValue={card.title}
                  required
                />
              </div>

              {/* Card Type */}
              <div className="grid gap-2">
                <Label htmlFor="type">Card Type</Label>
                <Input
                  id="type"
                  name="type"
                  type="text"
                  defaultValue={card.type}
                  required
                />
              </div>

              {/* Card Value */}
              <div className="grid gap-2">
                <Label htmlFor="value">Card Value ($)</Label>
                <Input
                  id="value"
                  name="value"
                  type="number"
                  min="0"
                  step="0.01"
                  defaultValue={card.value}
                  required
                />
              </div>

              {/* Points Required */}
              <div className="grid gap-2">
                <Label htmlFor="points">Points Required</Label>
                <Input
                  id="points"
                  name="points"
                  type="number"
                  min="0"
                  step="1"
                  defaultValue={card.points}
                  required
                />
              </div>
            </div>
          </form>
        </CardContent>

        <CardFooter className="flex justify-between gap-4">
          <Button variant="outline">
            <Link href={`/card-details/${card.id}`}>Cancel</Link>
          </Button>

          <Button type="submit" form="update-card-form">
            Save Changes
          </Button>
        </CardFooter>
      </Card>
    </main>
  );
}
