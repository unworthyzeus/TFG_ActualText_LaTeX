## Notes:

- The background/method should have the same structure as the results more or less. To find things easier when you don't understand; General framework (pipelines), path loss, angular spread and then delay spread. (For both background/method and results). Similar naming of the sub/sections between both. 
- Comparing the different models for the pathloss (channel attenuation) is cool. Add the same for angular and delay spread. In the results or a bit in SOA (without our results in the SOA).
- Maybe clarify actual inputs of the full framework model (only the topology/building heights and the height of the Tx), then the LoS/NLoS mask and the building/ground mask are computed. Those support maps feed the priors, which output five frozen prior maps: combined path loss, path-loss LoS, path-loss NLoS, delay spread, and angular spread. These, together with topology/masks and the scalar height conditioning path, feed the DL model. This has been clarified as two external framework inputs, nine spatial neural map channels plus a separate scalar UAV-height conditioning path, and three final output maps (PL, DS, AS).
- Use simple words when they are available (morphology, poly-whatever, etc.)
- Anyone should understand everything with just the thesis. But have a deeper knowledge with the appendix.
