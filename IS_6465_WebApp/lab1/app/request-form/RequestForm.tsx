"use client";
import React, { startTransition, useEffect } from "react";
import { format } from "date-fns";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Calendar } from "@/components/ui/calendar";
import {
  Popover,
  PopoverContent,
  PopoverDescription,
  PopoverHeader,
  PopoverTitle,
  PopoverTrigger,
} from "@/components/ui/popover";
import { Calendar as CalendarIcon } from "lucide-react";

export default function RequestForm() {
  const [date, setDate] = React.useState<Date | undefined>();

  useEffect(() => {
    startTransition(() => {
      setDate(new Date());
    });
  }, []);

  return (
    <div className="min-h-screen bg-linear-to-br from-slate-50 via-white to-blue-50 px-6 py-16">
      <div className="mx-auto flex max-w-6xl items-center justify-center">
        <Card className="w-full max-w-lg overflow-hidden rounded-2xl border-slate-200 bg-white shadow-xl">
          <CardHeader className="border-b bg-slate-50 px-6 py-6">
            <CardTitle className="text-2xl font-bold tracking-tight text-slate-900">
              Request a Tutoring Session
            </CardTitle>

            <CardDescription className="text-slate-600">
              Choose a date and tutor for your session.
            </CardDescription>
          </CardHeader>

          <CardContent className="space-y-6 px-6 py-6">
            <div className="space-y-2">
              <p className="text-sm font-medium text-slate-700">Session date</p>

              <Popover>
                <PopoverTrigger
                  render={
                    <Button
                      variant="outline"
                      data-empty={!date}
                      className="w-full justify-start text-left font-normal data-[empty=true]:text-muted-foreground"
                    />
                  }
                >
                  <CalendarIcon className="mr-2 h-4 w-4" />
                  {date ? format(date, "PPP") : <span>Pick a date</span>}
                </PopoverTrigger>

                <PopoverContent className="w-auto p-0">
                  <Calendar mode="single" selected={date} onSelect={setDate} />
                </PopoverContent>
              </Popover>
            </div>

            <div className="space-y-2">
              <p className="text-sm font-medium text-slate-700">Tutor</p>

              <Popover>
                <PopoverTrigger
                  render={
                    <Button
                      variant="outline"
                      className="w-full justify-between font-normal"
                    />
                  }
                >
                  Select a tutor
                </PopoverTrigger>

                <PopoverContent className="w-80">
                  <PopoverHeader>
                    <PopoverTitle>Select a tutor</PopoverTitle>
                    <PopoverDescription>
                      Choose from the currently available tutors.
                    </PopoverDescription>
                  </PopoverHeader>
                </PopoverContent>
              </Popover>
            </div>
          </CardContent>

          <CardFooter className="border-t bg-slate-50 px-6 py-4">
            <Button type="submit" className="w-full">
              Request Session
            </Button>
          </CardFooter>
        </Card>
      </div>
    </div>
  );
}
