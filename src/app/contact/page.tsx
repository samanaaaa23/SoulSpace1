// import Breadcrumb from "@/components/Common/Breadcrumb";
// import Contact from "@/components/Contact";

// import { Metadata } from "next";

// export const metadata: Metadata = {
//   title: "Contact Page | Free Next.js Template for Startup and SaaS",
//   description: "This is Contact Page for Startup Nextjs Template",
//   // other metadata
// };

// const ContactPage = () => {
//   return (
//     <>
//       <Breadcrumb
//         pageName="Contact Page"
//         description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. In varius eros eget sapien consectetur ultrices. Ut quis dapibus libero."
//       />

//       <Contact />
//     </>
//   );
// };

// export default ContactPage;

import Breadcrumb from "@/components/Common/Breadcrumb";
import Contact from "@/components/Contact";

import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact Us | SoulSpace - Music for the Soul",
  description: "Have questions or feedback? Reach out to SoulSpace and let us help you find harmony through music.",
  // other metadata
};

const ContactPage = () => {
  return (
    <>
      <Breadcrumb
        pageName="Contact Us"
        description="We’d love to hear from you! Whether it’s feedback, support, or collaboration, reach out and let SoulSpace be your guide to a more mindful musical journey."
      />

      <Contact />
    </>
  );
};

export default ContactPage;
