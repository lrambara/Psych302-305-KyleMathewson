# Week 7 — Laboratory Report
PSYCH 302/305 — Computational Methods in Psychology

## Part 1: Stroop Experiment

### Methods

#### Participants
One participant (myself) completed the experiment using a computer keyboard.

#### Materials
The experiment used four colour words: RED, BLUE, GREEN, and YELLOW. Each word appeared in coloured ink. The response keys were Z for red, X for blue, N for green, and M for yellow.

#### Procedure
The participant identified the ink colour rather than reading the word. Congruent trials had matching words and ink colours, while incongruent trials had different words and ink colours.

A fixation cross appeared for 500 ms before each stimulus, with a 500 ms gap between trials. The experiment included 8 practice trials followed by 40 scored trials (20 congruent and 20 incongruent), presented in randomized order.

Each stimulus remained visible until a response was made.

#### Data Handling
The experiment recorded the condition, word, ink colour, response key, accuracy, and reaction time in milliseconds.

Practice trials, incorrect responses, and reaction times below 150 ms or above 2500 ms were excluded from the reaction-time analysis.

Mean correct reaction times were calculated separately for congruent and incongruent trials. The Stroop effect was calculated as the incongruent mean minus the congruent mean.

### Results

I completed 40 scored trials in the Stroop task. Of these, 39 trials produced valid correct responses.

| Measure | Result |
|---|---|
| Scored trials | 40 |
| Valid correct trials | 39 |
| Mean congruent reaction time | 615 ms |
| Mean incongruent reaction time | 711 ms |
| Stroop effect | 96 ms |

The Stroop effect was calculated by subtracting the congruent mean from the incongruent mean:

711 − 615 = 96 ms

I responded 96 ms slower when the word and ink colour did not match, demonstrating the Stroop interference effect.

## Part 2: Hedge, Powell, and Sumner (2018)

### My Guess — Reconstructed Methods

Before reading the original Methods section, I predict that the researchers recruited adult participants to complete a computerized Stroop task.

Participants likely viewed colour words displayed in matching (congruent) or mismatching (incongruent) ink colours. They probably responded to the ink colour using assigned keyboard keys.

I predict that participants completed practice trials followed by randomized experimental trials, with approximately 40–100 trials per condition. Each participant was tested twice, approximately three weeks apart.

I expect the researchers excluded incorrect responses and unusually fast or slow reaction times.

The researchers likely calculated the Stroop effect by subtracting congruent reaction times from incongruent reaction times and examined how consistently participants performed across the two sessions.

### What I Missed

*To be completed after checking the original published Methods section.*

### Data Reanalysis

*To be completed after running analyze_stroop.py using the original exclusion rules and the course's 150–2500 ms rule.*

### Guesses, Misses, and Decisions

The Methods prediction was written before consulting the published Methods section. Differences between the predicted and actual procedure will be documented after reading the paper.

## AI Disclosure

I used ChatGPT to help organize and draft the laboratory report and to assist with implementing the Stroop experiment. I personally completed the Stroop task and collected my own reaction-time data. The Methods prediction and reanalysis will be checked against the course materials and actual analysis output.
