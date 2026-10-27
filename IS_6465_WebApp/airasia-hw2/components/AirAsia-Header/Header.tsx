import Image from "next/image";
import Link from "next/link";
import type { ReactNode } from "react";

type HeaderProps = {
  title: string;
  rightItems?: ReactNode[];
  navLinks?: ReactNode[];
};

const Header = ({ title, rightItems, navLinks }: HeaderProps) => {
  return (
    <header className="w-full border-b bg-white">
      <nav className="flex h-20 items-center justify-between px-6">
        {/* Left: Logo and Title */}
        <Link href="/" className="flex items-center gap-3">
          <Image
            src="/airasia-logo.png"
            alt="AirAsia Logo"
            width={64}
            height={64}
            priority
          />

          <span className="text-2xl font-bold text-gray-900">{title}</span>
        </Link>

        {/* Center: Navigation Links */}
        {/* <div className="flex items-center gap-6">
          {navLinks?.map((link, index) => (
            <div key={index}>{link}</div>
          ))}
        </div> */}

        {/* Right: Actions */}
        {/* <div className="flex items-center gap-4">
          {rightItems?.map((item, index) => (
            <div key={index}>{item}</div>
          ))}
        </div> */}
      </nav>
    </header>
  );
};

export default Header;
