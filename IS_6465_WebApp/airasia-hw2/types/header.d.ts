import type React from "react";

export type Url = string | URL;

declare global {
  type HeaderProps = {
    title: string;
    rightItems?: React.ReactNode[];
    navLinks?: React.ReactNode[];
  };

  // type MobileMenuProps = {
  //   rightItems?: React.ReactNode[];
  //   navLinks?: React.ReactNode[];
  // };

  // type NavLinkProps = {
  //   text: string;
  //   href?: Url;
  //   variant?: "desktop" | "mobile";
  //   dropdown?: boolean;
  //   items?: NavLinkDropdownProps[];
  // };
}

export {};
