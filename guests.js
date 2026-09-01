/* ============================================================
   THIS IS THE ONLY FILE YOU NEED TO EDIT.
   ============================================================

   1. EVENT  — the words on the page.
   2. BACKGROUNDS — the pool of images in the backgrounds/ folder.
   3. GUESTS — one line per person.

   Everyone on the GUESTS list automatically gets their own image
   from the pool, in order. Nobody shares. You just type names.
   ============================================================ */

const EVENT = {
  title: "Baby Shower",
  subtitle: "Pick your name to get your very own Zoom background",
  hostNote: "See you on the call! \u{1F37C}",
};

/* The image files, in the order they get handed out.
   Add more files to the backgrounds/ folder, then add the
   filename here so there are at least as many images as guests. */
const BACKGROUNDS = [
  "backgrounds/artist.jpg",
  "backgrounds/astronaut.jpg",
  "backgrounds/beachcomber.jpg",
  "backgrounds/beekeeper.jpg",
  "backgrounds/camper.jpg",
  "backgrounds/chef.jpg",
  "backgrounds/climber.jpg",
  "backgrounds/cowboy.jpg",
  "backgrounds/dinosaur.jpg",
  "backgrounds/duck.jpg",
  "backgrounds/explorer.jpg",
  "backgrounds/gardener.jpg",
  "backgrounds/king.jpg",
  "backgrounds/knitter.jpg",
  "backgrounds/magician.jpg",
  "backgrounds/mechanic.jpg",
  "backgrounds/pirate.jpg",
  "backgrounds/rockstar.jpg",
  "backgrounds/sherlock.jpg",
  "backgrounds/surfer.jpg",
];

/* One line per person. Just the name is enough.
   Tip: first name + last initial keeps the page a bit more private,
   since anyone with the link can read it.

   Want to hand-pick someone's image instead of letting it
   auto-assign? Write that line like this:
     { name: "Priya S.", background: "backgrounds/pirate.jpg" },
*/
const GUESTS = [
  // Jess gets the skiing one, pinned so it never gets handed to anyone else.
  // Upload it named skier.png and this lights up. (Any name works -- just
  // match it here; the page names the file it can't find.)
  { name: "Jess", background: "backgrounds/skier.jpg" },

  "Alex R.",
  "Sam T.",
  "Jordan K.",
  "Priya S.",
  "Miguel A.",
  "Dana W.",
  "Chris P.",
  "Nadia H.",
  "Tom B.",
  "Yuki M.",
  "Rachel G.",
  "Omar F.",
];
