# SPEAKER_NOTES.md

Word-for-word notes for the July 21 talk. Timestamps match `TIMELINE.md`.

## Opening (0:00 to 0:03)

**[Slide 1, title]**

> "Good evening. I'm Ahliana, the Principal Software Engineer at Ascentra. Thank you to Improving for hosting, PyTexas for sponsoring, and Dillon and Danyal for having me."

**[Slide 2, three QRs]**

> "Three QRs on screen. Discord on the left, my repo in the middle, my LinkedIn on the right. Take a second to scan.
>
> This is being recorded for the TechTalk YouTube channel. If you'd rather not appear on camera, sit toward the back."

**[Pause 15 seconds]**

> "Here's the deal. In the next 40 minutes, I'm going to give you x-ray glasses. Not for your language model. For your own code. By the end you'll see every prompt DSPy sent, every demonstration it picked, every instruction it rewrote. Then I'm going to take a prompt I hand-tuned over hours, and beat it. Twice. Live. On a metric. With plain Python.
>
> Three thirds. Ten minutes each. Declare, compose, tune. Let's fly."

## FIRST THIRD: DECLARE - Signatures (0:03 to 0:12)

**[Stay on Slide 3]**

> "Show of hands, who has hand-tuned a prompt for hours? Almost everyone. That's the crop duster. Low altitude, exhausting, and every model release wipes out your work."

**[Slide 4, signature]**

> "A DSPy signature looks like this. Five characters. Text in, sentiment out. I did not write a prompt. Let me prove it."

**[Notebook Cell 1]**

> "Run setup. 'Starship online.'"

**[Cell 2]**

> "Run the signature. Positive sentiment. I did not say 'be helpful.' I declared inputs and outputs."

**[Cell 3, x-ray glasses moment 1]**

> "Now the x-ray glasses. `inspect_history` shows me exactly what DSPy sent to the model. That's the prompt. I did not write it. The library wrote it from my signature.
>
> I edit signatures. I never edit prompts. That's the whole paradigm shift, in one sentence."

**[Cell 4, class form]**

> "More structure. Class-form signatures. Typed fields. Descriptions. Pydantic under the hood. Run it. Look, 'Houston we have a problem' came back classified as urgent. The model got the Apollo 13 reference."

**[Cell 5, the absurd one]**

> "Signatures do not police your intent. Watch."

**[Run. Audience laughs at the model trying to pick stocks from vibes.]**

> "The model gamely tries. Also a valid DSPy program. Weird in, weird out."

**[Slide 5, your turn]**

> "Your turn. Index card on your seat. Partner on your left, write the INPUTS. Partner on your right, write the OUTPUTS. Pick a real problem one of you has. 90 seconds. Go."

**[Timer, walk the room. At 90 seconds]**

> "Pencils down. Cards forward. I'll pick two."

**[Read two cards. NAME the authors.]**

> "First: [Name] and [Name] wrote inputs meeting transcript, output action items as a list. Excellent. Second: [Name] and [Name] wrote customer email, output sentiment and urgency. Also excellent. I'm holding one of these for later."

## MIDDLE THIRD: COMPOSE - Modules (0:12 to 0:21)

**[Slide 6, three modules]**

> "A signature describes WHAT. A module describes HOW.
>
> Three modules to know tonight. Predict, just asks the LM. ChainOfThought, model reasons out loud first. ReAct, model calls tools you give it.
>
> Same signature, different module, different behavior."

**[Cell 7, Predict vs ChainOfThought]**

> "Watch. Same signature, same input. Predict gives me the explanation. ChainOfThought gives me reasoning first, then the explanation. The reasoning field appeared automatically because I swapped one word in my code."

**[X-ray glasses moment 2]**

> "Glasses back on. Look at what ChainOfThought added to the prompt. There, an instruction to reason step by step. I did not write that. The library did."

**[Cell 8, code reviewer]**

> "Modules compose. Here's a real one. A code reviewer. Takes Python, returns a quality score, a list of issues, and improved code. This is a Signature plus a ChainOfThought. That's the entire program."

**[Run, walk through output. Read the score and issues from the screen.]**

> "Quality score right there. Issues: not using sum, no docstring, no validation. The improved version fixes them. Real code review."

**[Cell 9, swap models]**

> "One trick. I change one line, Haiku to Sonnet. Run it. Haiku said one thing, Sonnet said another with more depth. I did not rewrite any prompt. I did not change any logic. I changed the LM.
>
> That's the composition promise: portable across models."

**[Mid-talk lightning seed]**

> "Quick aside before the optimizer section. Hold a thought for me: ONE thing you could teach the rest of us in 5 minutes. Some Python thing you use, some bug you debugged, some library that saves you time. It comes back at the end."

## FINAL THIRD: TUNE - Optimizers + BEAT THE HAND-TUNED PROMPT (0:21 to 0:31)

**[Slide 7, the optimizer]**

> "Here's where I claimed I'd beat a hand-written prompt. I did not lie. Let's do it."

**[Cell 10, top portion]**

> "The task: classify a spacecraft transmission by urgency. Routine, attention, urgent. Here's the catch, and it's the whole point. On this team a CONFIRMED threat is urgent, but a SUSPECTED or unconfirmed hazard is only attention. You investigate first; you don't scramble. That's a convention. It lives in our data, not in common sense. Twelve training examples, ten held-out test examples, a metric that scores accuracy, and a baseline: plain Predict, no examples, no optimization."

**[Run baseline]**

> "Baseline classifies the test cabin fire as urgent. Good, but that's one example."

**[X-ray glasses moment 3]**

> "Glasses on. Plain prompt, no examples, no reasoning."

**[Score the baseline on all ten]**

> "Score it on all ten. Sixty percent. Common sense gets the confirmed emergencies and the coffee service. It misses the convention cases, and the misses print right there. Sixty is the number to beat. Remember it."

**[Cell 11, the hand-tuned prompt]**

> "Now the crop duster. Here's a prompt I wrote by hand. Role, categories, a strict safety policy, few-shot examples, format instructions. Every trick in the book, and it's a reasonable prompt.
>
> Watch safety rule two: if a hazard is not confirmed, treat it as urgent anyway. That's a sensible instinct for a flight controller.
>
> Let's measure it. Ten test transmissions."

**[Show accuracy result, about 60%]**

> "Hand-tuned prompt: sixty percent. The exact same score as no prompt at all. Hours of careful engineering, zero points gained. Look at the four misses on screen: every single one is an unconfirmed hazard my safety rule escalated."

**[X-ray glasses moment 4]**

> "Glasses on. Look at that safety rule. It escalates every unconfirmed hazard to urgent. A smoke detector that might be faulty, a possible leak, a suspected impact. My prompt marks all of them urgent. Our convention says those are attention, because you investigate first. My prompt encodes what I guessed. It cannot know a convention I never wrote down."

**[Cell 12, BootstrapFewShot LIVE]**

> "Now DSPy. No hand-tuning. Same twelve training examples, same metric. Before I run it, here's what it does: it runs my baseline on each training example, keeps the ones it gets right, and packs those correct examples into the prompt as demonstrations. Watch."

**[Run. It compiles in a few seconds.]**

> "That's it. A few seconds. Now we score it on the same ten test examples."

**[Show result, about 90%]**

> "Ninety percent. Same test set. Zero hand-tuning. It beat my careful prompt by thirty points."

**[X-ray glasses moment 5]**

> "Glasses on. Look at what BootstrapFewShot wrote. Demonstrations picked automatically from my labeled examples. Those examples carry the real convention, confirmed versus suspected, so the model learned the boundary I could not put into words. That's the beat. I did not write better rules. I let the data define the boundary."

**[Transition, MIPROv2 reveal]**

> "One more thing. BootstrapFewShot only picked examples. What happens when you let the optimizer rewrite the instruction too? That's MIPROv2. It takes a few minutes and more data, so I compiled it ahead of time on a forty-example training set."

**[Cell 12 second half, load artifact]**

> "Load the pre-compiled artifact. Run it on the same 10 test examples."

**[Show accuracy, 100%]**

> "One hundred percent. All ten, including the smoke detector that BootstrapFewShot missed. Sixty for my hand-tuned prompt, ninety for BootstrapFewShot, one hundred for MIPROv2."

**[X-ray glasses moment 6, the payoff]**

> "Glasses on, and this is the moment. Read what MIPROv2 wrote. It figured out the convention on its own. Confirmed plus a crisis is urgent. Hedging words, suspected, possible, intermittent, plus an investigative action, that's attention. Declarative past tense is routine.
>
> I never told it that rule. It found the boundary I could not put into words, and it wrote it down. That's the x-ray glasses and the optimizer in one screen. You do not write prompts. You let the data write them, and then you read exactly what it wrote.
>
> The cell pulls that instruction out clean at the bottom, so nobody has to squint at the dump."

**[Scoreboard cell]**

> "One picture. Sixty, sixty, ninety, one hundred. The gray bars are the crop duster: no prompt at all, and hours of hand-tuning, tied. The blue bars are the starship. That's the whole talk."

**[Audience proposal, 0:29:30]**

> "One last thing. I held back a card from earlier. [Name], [Name], let's run yours."

**[In Cell 6, type the signature live, run it]**

> "[Name], your program just ran on stage. Repo goes home with you. Adapt this pattern."

## Debrief (0:31 to 0:34)

**[Slide 8]**

> "Mission debrief.
>
> The repo. github.com/ahliana/dspy_starship. Clone it tonight.
>
> The method. There's a METHOD.md in the repo. Eight steps. Your Monday workflow.
>
> Related tools worth knowing. Arize Phoenix for observability. MCP for tool interop. pydantic-ai as a DSPy cousin. uv plus ruff for Python plumbing. Claude Code for terminal work.
>
> Sixty seconds. Turn to the person on your right. Introduce yourself. Trade LinkedIn if you want. Tell each other one thing you want to build with DSPy. Go."

**[60-second timer]**

## Lightning ask + closing (0:34 to 0:40)

**[Slide 9]**

> "One more thing. Lightning talks are up next. 4 minutes plus 1 for questions. The bar is lower than you think.
>
> Learned something this week? Lightning talk.
>
> Coworker asks how to do X? Lightning talk.
>
> Debugged something weird at 2am? Definitely a lightning talk.
>
> [Name], [Name], [Name], what you proposed on those cards tonight, that IS a lightning talk. Sign up at the door.
>
> Thanks to Dillon and Danyal for running PyHou. Thanks to Improving for the space, PyTexas for the support. Thanks to all of you for being here."

**[Slide 10, thank you / Q&A]**

> "Questions?"

## Q&A (0:40 to 0:50)

For each question:
1. Let them finish
2. **Repeat the question** for YouTube
3. Answer in under 60 seconds
4. Deep question: "Short answer is X, let's continue in Discord"
5. Unknown: "I don't know off the top. Anyone in the room? If not, drop it in Discord."

**Seed questions if Q&A stalls at 0:42:**

Pretend the question came from the room. Introduce with: "Someone earlier asked me..."

1. **"How is this different from writing a good prompt?"** In prompt engineering, the prompt IS the artifact. In DSPy, the signature and the examples are the artifact. The library compiles them into a prompt. When you want to improve, you change the signature, not the prompt.

2. **"When would I use DSPy over LangChain or LlamaIndex?"** When prompt quality is the thing you want to improve. LangChain and LlamaIndex wire components together. DSPy makes the components themselves better. They coexist.

3. **"Does it work with models other than Anthropic?"** Yes. LiteLLM under the hood. OpenAI, Anthropic, Gemini, local via Ollama. Change the string.

4. **"How big does the training set need to be?"** BootstrapFewShot works with 5 to 20. MIPROv2 wants 20 to 200. You need inputs and a metric. Labels help but aren't always required.

5. **"What is MIPROv2 doing inside?"** Bayesian optimization over instruction proposals and demonstration sets. Uses a meta-LM to propose instructions, runs the program on the dev set, picks best combinations, iterates.

6. **"Would DSPy beat a genuinely good prompt? Isn't yours a strawman?"** The prompt follows best practice: role, categories, a policy, examples, format rules. It loses because its safety policy guesses a convention that doesn't match the data, and plain Predict with no prompt also scored sixty. On tasks the model already handles, a good prompt and DSPy tie, and the win is speed and portability instead of accuracy. The gap opens whenever the right answer depends on your team's convention, which is most real business tasks.

## Closing at 0:50 (7:30 PM)

> "Thank you. Repo is on the screen. Find me at the back. Lightning talks are up next."

**[Off stage]**

## Recognition checklist

Before walking off, check:
- [ ] Named the two index card authors from segment 2
- [ ] Named the audience-voted proposal author from segment 4
- [ ] Named 2+ question-askers from Q&A
- [ ] Thanked Dillon and Danyal by name
- [ ] Thanked Improving and PyTexas
- [ ] Pointed to the TechTalk operator
