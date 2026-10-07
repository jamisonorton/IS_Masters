import { Metadata } from "next";
import RequestForm from "./RequestForm";

export const metadata: Metadata = {
  title: "Request Form",
};

export default function Request() {
  return (
    <div>
      <RequestForm />
    </div>
  );
}
