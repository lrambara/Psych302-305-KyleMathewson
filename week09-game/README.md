# Week 9 · Make a game

**Name:** Luca Rambaransingh  
**Date of class:** 4 November 2026  
**Lab page:** https://kylemath.github.io/Psych302-305-KyleMathewson/game.html

---

## 1. My game (3 points)

My game is called *Jungle Scream Challenge*. To play, you allow microphone access and shout "BANANA!" whenever a banana appears in the canopy. You have to stay silent when a coconut appears, and the game progressively gets faster as you advance through the levels.

## 2. What I changed (3 points)

1. **Game Title:** I changed the game's title from "In the Canopy" to "Jungle Scream Challenge" to give it a different identity.

2. **Instructions and Microphone Feedback:** I modified the instructions and feedback messages to emphasize shouting rather than simply saying "banana". I also changed the starting message to make the objective clearer and encourage players to speak louder when they weren't reaching the microphone threshold.

3. **End-of-Game Performance Summary:** I modified the `gameOver()` function to calculate the number of correct trials and overall accuracy using the recorded `data` array. The game now displays these statistics when it ends, giving players immediate feedback about their performance. I added this feature after collecting my original results, so it did not affect the gameplay or CSV data.

## 3. My guess, then my data (2 points)

**My guess (written before playing):**

I predicted that I would miss more bananas when they were deeper in the jungle or heavily covered by leaves. I also expected my accuracy to decrease as the levels became faster because I would have less time to recognize the fruit and respond.

**What happened:**

I completed 31 trials and finished with a score of 195 points. I correctly responded to 24 out of 31 trials, giving me an overall accuracy of 77.4%.

My accuracy decreased across the levels:

- Level 1: 90% (9/10)
- Level 2: 80% (8/10)
- Level 3: 70% (7/10)
- Level 4: 0% (0/1)

I correctly avoided all 9 coconuts but missed 7 out of 22 bananas. My average recorded reaction time was approximately 714 milliseconds.

I also performed worse when objects were deeper in the canopy. At depth 1, I was correct on 11 out of 12 trials, compared to only 5 out of 10 trials at depth 3. This was consistent with my prediction that deeper objects would be more difficult to identify.

Overall, my results were consistent with my predictions, although I would need more trials to determine whether these patterns were reliable.

## 4. One reason not to trust it (1 point)

One limitation is that I was the only participant and completed just one session. My performance could have been influenced by practice or fatigue, so these results might not represent how other people would perform.

## 5. Use of AI (1 point)

- **Did you use an AI tool?** Yes, ChatGPT.
- **What did you ask, what did you keep, and what did you change?**

I used ChatGPT to help modify the starter game's code, troubleshoot GitHub, analyze my CSV results, and organize my README. I kept the original gameplay mechanics and jungle environment while changing the title, instructions, and microphone feedback. I also added an end-of-game performance summary with AI assistance. I played the game myself and collected the results directly from its CSV export.

## Could this be part of your project? (optional, no points)

Yes, I could adapt the microphone-based gameplay into a VR experiment investigating whether shouting or vocal intensity affects reaction time and performance.
