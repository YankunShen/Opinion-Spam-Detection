# Opinion-Spam-Detection

1. Load in and combine all the data
    * combine all the _.txt_ files in different folder to a _.txt_ file
    * convert **txt** file to **csv** file
    * create a csv file -- label (1: **non-spam**  -1: **spam**)
    * add the label as a column to previous csv files
    
2. Data Processing 
    * replace num with 'N'
    * Eliminate special character
    * Space out punctuation
    * Trim
    * Remove additional white spaces
3. Data Visualization
    * lens of each review in histogram
    * sentiment analysis
    * Show the frequency of words in deceptive and truthful reviews using _scattertext_ library.
    
4. Use Kashgari(*https://kashgari.bmio.net*)
    >Kashgari is a simple and powerful NLP Transfer learning framework, build a state-of-art model in 5 minutes for named entity recognition (NER), part-of-speech tagging (PoS), and text classification tasks.
 
 5. Load the pretrained BERT Model checkpoint
    * Load the dataset
    * Load BERT embedding
    * Tokenize data
 
 6. Build the Model and Evaluate