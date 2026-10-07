import { Metadata } from "next";
import RequestForm from "./RequestForm";

export const metadata: Metadata = {
  title: "Request Form",
};

const Request = () => {
  return (
    <div>
      <RequestForm />
    </div>
  );
};

export default Request;
