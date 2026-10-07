import Link from "next/link";
import { GraduationCap } from "lucide-react";

const Navbar = () => {
  return (
    <nav className="fixed top-0 w-full flex items-center justify-around py-5 px-24 border-b border-gray-700 bg-gray-700">
      <Link
        href="/"
        className="transistion duration-300 hover:scale-110 text-gray-200 hover:text-white"
      >
        <GraduationCap />
      </Link>

      <ul className="flex gap-10 text-lg">
        <Link
          href="/tutors"
          className="text-gray-200 hover:text-white transition-colors"
        >
          Tutors
        </Link>
      </ul>
    </nav>
  );
};

export default Navbar;
