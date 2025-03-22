import { Feature } from "@/types/feature";

const featuresData: Feature[] = [
  {
    id: 1,
    icon: (
      <svg width="40" height="40" viewBox="0 0 40 40" className="fill-current">
        <path
          opacity="0.5"
          d="M20 1.667C9.875 1.667 1.667 9.875 1.667 20S9.875 38.333 20 38.333 38.333 30.125 38.333 20 30.125 1.667 20 1.667Z"
        />
        <path d="M26.667 20a6.667 6.667 0 11-13.334 0 6.667 6.667 0 0113.334 0z" />
      </svg>
    ),
    title: "Mood-Based Music Player",
    paragraph:
      "SoulSpace curates playlists based on your mood.",
  },
  {
    id: 2,
    icon: (
      <svg width="40" height="40" viewBox="0 0 40 40" className="fill-current">
        <path
          opacity="0.5"
          d="M20 0C8.954 0 0 8.954 0 20s8.954 20 20 20 20-8.954 20-20S31.046 0 20 0z"
        />
        <path d="M13.333 20h13.334M20 13.333v13.334" />
      </svg>
    ),
    title: "Daily Mindfulness Notifications",
    paragraph:
      "Receive daily reminders for mindfulness, meditation, and inspirational quotes.",
  },
  {
    id: 3,
    icon: (
      <svg width="40" height="40" viewBox="0 0 40 40" className="fill-current">
        <path
          opacity="0.5"
          d="M20 2.5C10.887 2.5 3.333 10.054 3.333 19.167c0 7.017 4.536 13.04 10.833 15.365V37.5h12.5v-3.833c6.297-2.325 10.833-8.348 10.833-15.365C36.667 10.054 29.113 2.5 20 2.5z"
        />
      </svg>
    ),
    title: "Offline & Ad-Free Experience for Music.",
    paragraph:
      "Upgrade to the pro version for offline access, ad-free music, and premium mindfulness content.",
  },
  {
    id: 4,
    icon: (
      <svg width="40" height="40" viewBox="0 0 40 40" className="fill-current">
        <path
          opacity="0.5"
          d="M20 0C8.954 0 0 8.954 0 20s8.954 20 20 20 20-8.954 20-20S31.046 0 20 0z"
        />
        <path d="M15 25l10-10M25 25l-10-10" />
      </svg>
    ),
    title: "Integrated Journaling Feature",
    paragraph:
      "Write reflections, set mindfulness goals, and track your progress with the built-in journaling feature.",
  },
  {
    id: 5,
    icon: (
      <svg width="40" height="40" viewBox="0 0 40 40" className="fill-current">
        <path
          opacity="0.5"
          d="M20 0C8.954 0 0 8.954 0 20s8.954 20 20 20 20-8.954 20-20S31.046 0 20 0z"
        />
        <path d="M15 25l10-10M25 25l-10-10" />
      </svg>
    ),
    title: "Meditation Sessions",
    paragraph:
      "Take our meditation sessions, set a goal and track your progress.",
  },
];

export default featuresData;
