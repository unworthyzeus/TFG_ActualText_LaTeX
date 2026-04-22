### This is a summary of things I've been thinking that need to be included it in the thesis.

- How the dataset is structured, image size, everything that it contains (topology, LoS mask, path loss, delay spread, angular spread, antenna height by sample, sample number and city)
- Original goals <20º rmse for angular spread, <50ns rmse for delay spread, <5dB rmse for path loss (global nLoS plus LoS results)
- First approach of UNet + CGAN, doesn't work, retry.
- Different approaches before changing architecture like upsampling, etc (see Try 22).
- How CGAN didn't make a difference.
- How separating models didn't work (like separating delay spread and angular spread and path loss prediction, nor separating LoS from nLoS originally)
- The research of the first priors, how they failed catastrophically on nLoS (as all the models were already doing anyways, so I didn't see anything wrong). 
- How the different priors were tried, the SOA of try 66 (the LaTeX document), obstruction, new architectures of tries 50-75 (aprox).
- How after try 75 I said, I need to change something drastic, looked at the histograms, saw that it wasn't fitting nLoS. Decided to change the architecture to first predicting the distribution (explain in detail) and then doing a UNet to say what pixel is each value from the distribution.
- Why this worked WONDERS for nLoS, but didn't improve LoS (in fact made it slightly worse), see Try 76.
- How this approached worked mightly well for improving global and per expert results for the angular and delay spreads for try 77. (It doesn't work as well because the distribution are much less Gaussian and vary a lot between samples)
- How after knowing that good nLoS performance was actually possible I improved (and how I did it), the priors callibrating them correctly and getting 3dBs (aprox) on nLoS and 1.75 dB on LoS, getting 1.95dB rmse. (also citing papers)
- How try 79 makes the delay spread and angular spread prior with good results (citing papers).
- How try 80 mixes everything again, architecture of try 76 and 77 but with priors of 78 and 79. One mega model for everything.
- How the split between experts works on tries 76, 77 and 80 (also mentioning that in fact for the prior there are more, see try 78 and 79). Maybe explaining differences with other splits I did, and also mentioning that it's good practices, not bad.
- How the split between training, validation and testing works for tries 76, 77 and 80 (it's the same and the final one). Say why is it good and put some examples of differences between bad practices, and decent practices but not so good of other ones.
- How the sinusoidal film conditioning works and why.
- Full schema of the final tries (76-80), model architecture, etc. Like diagrams of the diagrams folder in TFGPractice.
- What to do next (varying frequencies!! for a general outdoors CKM (channel knowledge map) model)
- That I used 4 GPUs (RTX 2080ti) plus good GPUs (let's say 1500W total aprox) for 12 hours for the final try, about 18 for tries 76-79, and over 200 for all tries, but these should not be counted. (There is a section on how good for the environment the project is , see sustainability, our project is actually good because we now don't need simulations, we compute CKM with great accuracy and with much less energy and time)
- What are we doing new and differently in general.
- There are panels, samples, already taken from the dataset to compare them, they are good and bad cases for the prior, take more from the dataset in the style if necessary



### How to

- First, make a structured copy of this document, as a checklist to mark the ones you complete.
- Then investigate with, probably subagents, there is A LOT of information on this project, I'd say copy ALL (even inside nested folders) .md files to know everything, priority on newer/later tries .md files. Then, research papers online if you need to.
- For any doubts, ask me.
- Research TFGs from ETSETB if you want to.
- Start working, put the acronyms in acronyms.tex as you keep putting them in the document (CKM, nLoS, etc.)
- For any doubts, ask me.
- The acknowledgemtns and dedication I'll do them myself.
- Tell me when you finish.


### Style specifications

- Use the same style and format as the baseline already in the project
- Use figures, create them new or recycle from the project
- Number the figures, equations, etc.