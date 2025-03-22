

import Image from "next/image";

const AboutSectionTwo = () => {
  return (
    <section className="py-16 md:py-20 lg:py-28 bg-gradient-to-b from-[#101C41] to-[#1A2950] text-white">
      <div className="container mx-auto">
        <div className="flex flex-wrap items-center">
          
          {/* Left Side - Updated Image Section */}
          <div className="w-full px-6 lg:w-1/2 flex justify-center">
            <div className="relative max-w-[500px]">
              <Image
                src="/images/about/art.png" 
                alt="SoulSpace Experience"
                width={500}
                height={500}
                className="rounded-xl shadow-lg"
              />
            </div>
          </div>

          {/* Right Side - Features Section */}
          <div className="w-full px-6 lg:w-1/2">
            <h2 className="text-3xl font-bold mb-6">Why Choose SoulSpace?</h2>
            
            {/* Feature 1 */}
            <div className="mb-6 flex items-center">
              <Image
                src="/images/about/music.jpg"
                alt="Mood-Based Music"
                width={40}
                height={40}
                className="mr-4"
              />
              <div>
                <h3 className="text-xl font-semibold">Personalized Music for Every Mood</h3>
                <p className="text-gray-300">
                  Let SoulSpace curate music that aligns with your mood—happy, sad, romantic, study, or meditation.
                </p>
              </div>
            </div>

            {/* Feature 2 */}
            <div className="mb-6 flex items-center">
              <Image
                src="/images/about/mindfulness.jpg" 
                alt="Mindfulness Reminders"
                width={40}
                height={40}
                className="mr-4"
              />
              <div>
                <h3 className="text-xl font-semibold">Mindfulness Sessions and Reminders</h3>
                <p className="text-gray-300">
                  Stay consistent with daily mindfulness sessions, reminders, and alerts.
                </p>
              </div>
            </div>

            {/* Feature 3 */}
            <div className="mb-6 flex items-center">
              <Image
                src="/images/about/noad.jpg" 
                alt="Ad-Free & Offline Mode"
                width={40}
                height={40}
                className="mr-4"
              />
              <div>
                <h3 className="text-xl font-semibold">No Ads & Offline Music for Premium Users</h3>
                <p className="text-gray-300">
                  Enjoy an uninterrupted experience with premium benefits.
                </p>
              </div>
            </div>

            <div className="flex items-center">
              <Image
                src="/images/about/journaling.jpg" 
                alt="Journaling"
                width={40}
                height={40}
                className="mr-4"
              />
              <div>
                <h3 className="text-xl font-semibold">Journaling</h3>
                <p className="text-gray-300">
                Capture your thoughts, track your emotions, and cultivate mindfulness through journaling. 
                With <strong>SoulSpace</strong>, you can <strong>write freely, revisit past entries, 
                and track your personal growth</strong>—one entry at a time.
                </p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
};

export default AboutSectionTwo;
