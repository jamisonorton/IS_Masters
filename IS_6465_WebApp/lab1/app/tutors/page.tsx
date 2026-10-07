import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Tutors",
};

export default function tutors() {
  return (
    <div>
      <table>
        <caption>Available tutors</caption>
        <thead>
          <tr>
            <th>Name</th>
            <th>Course</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Maya</td>
            <td>IS 6465</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
