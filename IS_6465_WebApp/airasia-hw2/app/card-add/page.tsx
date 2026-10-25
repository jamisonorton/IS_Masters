import Link from "next/link";

import { Button, buttonVariants } from "@/components/ui/button";
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

export default function CardAdd() {
  return (
    <main className="flex flex-1 flex-col gap-6 bg-zinc-50 p-6 dark:bg-black">
      <h1 className="text-4xl font-bold">Add Gift Card</h1>

      <Card className="w-full max-w-xl">
        <CardHeader>
          <CardTitle>New Gift Card</CardTitle>
          <CardDescription>
            Enter the gift card information below.
          </CardDescription>
        </CardHeader>

        <CardContent>
          <form id="add-card-form" action="/card-list" method="GET">
            <div className="flex flex-col gap-6">
              {/* Card Name */}
              <div className="grid gap-2">
                <Label htmlFor="title">Card Name</Label>
                <Input
                  id="title"
                  name="title"
                  type="text"
                  placeholder="e.g. AirAsia e-Gift Card"
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
                  placeholder="e.g. Electronic or Physical"
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
                  placeholder="e.g. 25"
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
                  placeholder="e.g. 2500"
                  required
                />
              </div>
            </div>
          </form>
        </CardContent>

        <CardFooter className="flex justify-between gap-4">
          <Link
            href="/card-list"
            className={buttonVariants({
              variant: "outline",
            })}
          >
            Cancel
          </Link>

          <Button type="submit" form="add-card-form">
            Add Gift Card
          </Button>
        </CardFooter>
      </Card>
    </main>
  );
}
