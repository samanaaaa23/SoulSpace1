"use client";
import Link from "next/link";

const Footer = () => {
  return (
    <footer className="relative z-10 bg-white pt-16 dark:bg-gray-dark md:pt-20 lg:pt-24">
      <div className="container">
        <div className="-mx-4 flex flex-wrap">
          <div className="w-full px-4 md:w-1/2 lg:w-4/12 xl:w-5/12">
            <div className="mb-12 max-w-[360px] lg:mb-16">
              <Link href="/" className="mb-8 inline-block">
                <p className="text-3xl font-bold text-white lg:text-2xl">SoulSpace</p>
              </Link>
              <p className="mb-9 text-base leading-relaxed text-body-color dark:text-body-color-dark">
                Close your eyes, breathe in the melodies. SoulSpace curates sounds that move with you—whether in joy, reflection, or solitude.
              </p>
              <div className="flex items-center space-x-6">
                {["facebook", "twitter", "youtube", "linkedin"].map((platform, index) => (
                  <a
                    key={index}
                    href="/"
                    aria-label={platform}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-body-color duration-300 hover:text-primary dark:text-body-color-dark dark:hover:text-primary"
                  >
                    <i className={`fab fa-${platform} text-xl`}></i>
                  </a>
                ))}
              </div>
            </div>
          </div>

          {["Useful Links", "Terms", "Support & Help"].map((section, index) => (
            <div key={index} className="w-full px-4 sm:w-1/2 md:w-1/2 lg:w-2/12 xl:w-2/12">
              <div className="mb-12 lg:mb-16">
                <h2 className="mb-10 text-xl font-bold text-black dark:text-white">{section}</h2>
                <ul>
                  {section === "Useful Links" && ["Blog", "Pricing", "About"].map((link) => (
                    <li key={link}>
                      <Link href={`/${link.toLowerCase()}`} className="mb-4 inline-block text-base text-body-color duration-300 hover:text-primary dark:text-body-color-dark dark:hover:text-primary">
                        {link}
                      </Link>
                    </li>
                  ))}
                  {section === "Terms" && ["TOS", "Privacy Policy", "Refund Policy"].map((link) => (
                    <li key={link}>
                      <Link href={`/${link.replace(/ /g, "").toLowerCase()}`} className="mb-4 inline-block text-base text-body-color duration-300 hover:text-primary dark:text-body-color-dark dark:hover:text-primary">
                        {link}
                      </Link>
                    </li>
                  ))}
                  {section === "Support & Help" && ["Open Support Ticket", "Terms of Use", "About"].map((link) => (
                    <li key={link}>
                      <Link href={`/${link.replace(/ /g, "").toLowerCase()}`} className="mb-4 inline-block text-base text-body-color duration-300 hover:text-primary dark:text-body-color-dark dark:hover:text-primary">
                        {link}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          ))}
        </div>
        <div className="h-px w-full bg-gradient-to-r from-transparent via-[#D2D8E183] to-transparent dark:via-[#959CB183]"></div>
        <div className="py-8 text-center text-sm text-body-color dark:text-body-color-dark">
          &copy; {new Date().getFullYear()} SoulSpace. All rights reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
