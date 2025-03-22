import Image from "next/image";

const AboutSectionTwoPartOne = () => {
  return (
    <section className="py-16 md:py-20 lg:py-28">
      <div className="container">
        <div className="-mx-4 flex flex-wrap items-center">
          <div className="w-full px-4 lg:w-1/2">
            <div className="max-w-[470px]">
              <div className="mb-9">
                <h3 className="text-xl font-bold text-black dark:text-white">
                  Create a Mindful Routine
                </h3>
                <p className="text-base font-medium text-body-color">
                  Set your daily mindfulness reminders and build a habit of inner peace.
                </p>
              </div>
              <div className="mb-9">
                <h3 className="text-xl font-bold text-black dark:text-white">
                  Journaling for Reflection
                </h3>
                <p className="text-base font-medium text-body-color">
                  Express yourself and track your emotions with our built-in journal.
                </p>
              </div>
            </div>
          </div>
          <div className="w-full px-4 lg:w-1/2">
            <Image
              src="/images/about/Journaling.jpg"
              alt="Journaling Feature"
              fill
              className="drop-shadow-three dark:hidden"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSectionTwoPartOne;
