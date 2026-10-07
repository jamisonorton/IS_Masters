import Image from "next/image";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Peer Tutoring Hub",
};

export default function HomePage() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="space-y-3 max-w-3xl">
        <h1 className="text-5xl font-semibold">Peer Tutoring Hub</h1>
        <Image
          src="/images/tutoring.png"
          alt="Student meeting with a peer tutor"
          loading="eager"
          width={500}
          height={500}
        />
      </div>
    </div>
  );
}
