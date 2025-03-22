// import AboutSectionOne from "@/components/About/AboutSectionOne";
// import AboutSectionTwo from "@/components/About/AboutSectionTwo";
// import Breadcrumb from "@/components/Common/Breadcrumb";

// import { Metadata } from "next";

// export const metadata: Metadata = {
//   title: "About SoulSpace | Elevate Your Music & Mindfulness",
//   description:
//     "SoulSpace is a music recommendation platform designed to harmonize your emotions with sound, bringing mindfulness and serenity into your daily life.",
// };

// const AboutPage = () => {
//   return (
//     <>
//       {/* Breadcrumb with Engaging Introduction */}
//       <Breadcrumb
//         pageName="Discover SoulSpace"
//         description="Step into a world where music meets mindfulness. At SoulSpace, we curate sounds that heal, inspire, and elevate your emotions—because every moment deserves the perfect melody."
//       />

//       {/* About Sections */}
//       <section className="relative bg-gradient-to-b from-[#1a1a2e] to-[#16213e] text-white py-20">
//         <div className="container mx-auto text-center">
//           <h2 className="text-4xl font-extrabold mb-4">Our Story</h2>
//           <p className="text-lg max-w-2xl mx-auto opacity-80">
//             SoulSpace was born from the idea that music is more than just sound—it’s a journey.
//             We blend AI-driven recommendations with mindfulness practices, offering a personalized
//             space to immerse yourself in melodies that resonate with your soul.
//           </p>
//         </div>
//       </section>

//       <AboutSectionOne />
//       <AboutSectionTwo />

//       {/* Call to Action Section */}
//       <section className="bg-[#0f3460] text-white py-16 text-center">
//         <div className="container mx-auto">
//           <h3 className="text-3xl font-semibold mb-3">Start Your Soulful Journey Today</h3>
//           <p className="mb-6 opacity-80">
//             Whether you seek calm, focus, or inspiration, let SoulSpace be your guide.
//           </p>
//           <a
//             href="/register"
//             className="px-6 py-3 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg text-lg font-medium transition-transform transform hover:scale-105"
//           >
//             Join SoulSpace Now
//           </a>
//         </div>
//       </section>
//     </>
//   );
// };

// export default AboutPage;

import AboutSectionOne from "@/components/About/AboutSectionOne";
import AboutSectionTwo from "@/components/About/AboutSectionTwo";
import Breadcrumb from "@/components/Common/Breadcrumb";

import { Metadata } from "next";

export const metadata: Metadata = {
  title: "About SoulSpace | Elevate Your Music & Mindfulness",
  description:
    "SoulSpace is a music recommendation platform designed to harmonize your emotions with sound, bringing mindfulness and serenity into your daily life.",
};

const AboutPage = () => {
  return (
    <>
      {/* Breadcrumb with Engaging Introduction */}
      <Breadcrumb
        pageName="Discover SoulSpace"
        description="Step into a world where music meets mindfulness. At SoulSpace, we curate sounds that heal, inspire, and elevate your emotions—because every moment deserves the perfect melody."
      />

      {/* About Sections
      <section className="relative bg-gradient-to-b from-[#1a1a2e] to-[#16213e] text-white py-20">
        <div className="container mx-auto text-center">
          <h2 className="text-5xl font-extrabold mb-6 tracking-wide">Our Story</h2>
          <p className="text-xl font-serif max-w-2xl mx-auto opacity-90 leading-relaxed">
            SoulSpace was born from the idea that music is more than just sound—it’s a journey.
            We blend AI-driven recommendations with mindfulness practices, offering a personalized
            space to immerse yourself in melodies that resonate with your soul. Here, every note is
            crafted to align your emotions with the perfect soundtrack for your life.
          </p>
        </div>
      </section> */}

      <AboutSectionOne />
      <AboutSectionTwo />

      {/* Call to Action Section */}
      <section className="from-[#101C41] to-[#1A2950] text-white py-16 text-center">
        <div className="container mx-auto">
          <h3 className="text-3xl font-semibold mb-3">Start Your Soulful Journey Today</h3>
          <p className="mb-6 opacity-80">
            Whether you seek calm, focus, or inspiration, let SoulSpace be your guide.
          </p>
          <a
            href="/register"
            className="px-6 py-3 bg-[#7a9aca] rounded-lg text-lg font-medium transition-all duration-300 transform hover:bg-[#1a2a3d] hover:scale-105 hover:text-white"
          >
            Join SoulSpace Now
          </a>
        </div>
      </section>
    </>
  );
};

export default AboutPage;
