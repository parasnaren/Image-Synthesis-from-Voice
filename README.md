# Image-synthesis-from-voice

Synthesis of images, primarily of birds from textual description using GANs


### Dependencies
- PyTorch
- Pillow
- easydict


### Run code

1.  Navigate to `Voice2Image/text-to-image/`
2.  Run the `Text-to-Image.ipynb` jupyter notebook
3.  To run the program, follow either of the below steps:

    -  Run `generate_bird(text)` function by passing some descriptive text for birds as a parameter *Eg: This is a red bird that has black wings and a white beak*


    -  Run `generate(text)` function by passing any random description of any object(s). *Note: Results aren't the best for generic descriptions*


    -  Run `run_app()` and speak into the microphone for not more than 5 secs with either description of a bird or something generic. *Note: Key word being 'bird' to be said in order to generate images of birds*


*Note: Configurations for the model can be altered in the notebook to run on different version of the models*

Additionally run `speech_text.ipynb` to transcribe voice into text.
