Machine Learning Algorithms
---

Algorithm | Type    | Best Use Case | Key Formula / Logic | Assumptions | Pros  | Cons  | When not to use | Real world example
---         | ---   | ---           | ---                   | ---       | ---   | ---   | ---               |   ---
Linear Regression | Supervised | Predicting continous values | | Linearity, independence | Simple, interpretable, fast | Sensitive to outliers, non-linear limits | Data with strong non-linearity | House price prediction
Logistic Regression | Supervised | Binary classification |  | Log-odds linearity | Probabilistic, interpretable | Weak with non-linear boundaries | Data is highly non-linear | Spam detection
Decision Tree | Supervised | Classification / Regression | Recursive binary split | None | Easy to interpret | Overfitting, unstable | Noisy or complex datasets | Loan default prediction
Random Forest | Supervised | Ensemble accuracy | Bagging + overaging trees | Tree independence | High accuracy, robust | Slower, less interpretable | Need real-time results | Fraud detection
Gradient Boosting | Supervised | High performance modeling | Additive trees minimizing loss | Sequential dependency | State-of-the-art accuracy | Overfittig, needs tuning | When interpretability matters | Credit scoring
SVM | Supervised | Max-margin classification | Maximize margin using kernel trick | Separability, scaling | Works in high dimensions | Slow on large data | Large noisy datasets | Facial recognition
KNN | Supervised | Few-shot classification | Distance-based majority vote | Feature scaling | Simple, no training phase| Slow, noisy sensitive | High-dimensional noisy data | Recommender systems
Naive Bayes | Supervised | Text classification | Bayes theorem + feature independence | Independent features | Fast, good with text data | Fails with correlated features | Feature dependency present | Sentiment analysis
K-Means | UnSupervised | Customer segmentation | Minimize intra-cluster distance | Spherical, equal cluster | Fast, easy to implement | Needs K, sensitive to scale | Non-spherical data | Customer segmentation
Hierarchical Cluster | UnSupervised | Data structure understanding | Nested dendrogram | Distance metric | No need for K, visual | Memroy and compute intensive | Very large datasets | Gene expression analysis
PCA | Dim. Reduction | Reducing feature dimensionality | Eigevectors of covariance matrix | Large variance important | Noise reduction, speed-up | Hard to interpret | All features are important | Image compression
Neural Networks (MLP) | Supervised | Complex pattern modeling | Weighted sums + activation functions | Enought data, scaling | Non-linear learning power | Needs large data & tuning | Small data, low compute | Image compression
CNN | Supervised | Image/video/spatial data | Convolution + pooling layers | Grid-like spatial data | Excellent for images | High resource demand | Sequence/text data | Self-driving vision
RNN | Supervised | Sequence modeling | Feedback loops over time | Sequential structure | Time-series & text ready | Vanishing gradient | Long sequeces | Stock prediction
Transformer (BERT, GPT) | Supervised / Self-supervised | NLP tasks, chat, translation | Attention mechanism + position encoding | Large training data | Long context, fast | Heavy compute, large model | Small projects | Chat GPT, Translation tools
Autoencoders | UnSupervised | Compression, anamoly detection | Encoder-decoder + reconstruction loss | Symmetric network | Effective denoising | Can overfit, black-box | When no compression needed | Fraud detection
DBSCAN | UnSupervised | Arbitrary shape clustering | Density-based region growing | Cluster density | Noise tolerant, shape-flexible | Fails on varying density | Sparse high-dim data | Geo-spatial clustering
