# Stock Price Prediction Using CNN - Technical Documentation

## Model Implementation and Results

### 1. Data Preprocessing
```python
# Input shape: (1320, 60, 10)
# - 1320 training sequences
# - 60 time steps per sequence
# - 10 features per time step

Features implemented:
1. Price indicators:
   - Close price
   - Moving averages (MA5, MA20, MA50)
   - Daily returns
   - Returns over 5 days

2. Volume indicators:
   - Raw volume
   - Volume moving averages (5-day, 20-day)

3. Volatility metrics:
   - 20-day rolling standard deviation
   - Daily price range
   - Daily range percentage
```

### 2. Model Architecture
```python
CNN Model Structure:
1. Input Layer: (60, 10) - 60 timesteps, 10 features

2. First CNN Block:
   - Conv1D(32 filters, kernel_size=3, activation='relu')
   - BatchNormalization()
   - MaxPooling1D(pool_size=2)
   - Dropout(0.2)

3. Second CNN Block:
   - Conv1D(64 filters, kernel_size=3, activation='relu')
   - BatchNormalization()
   - MaxPooling1D(pool_size=2)
   - Dropout(0.2)

4. Dense Layers:
   - Flatten()
   - Dense(50, activation='relu')
   - BatchNormalization()
   - Dropout(0.2)
   - Dense(1) # Output layer

Total Parameters: 49,485
- Trainable params: 49,193
- Non-trainable params: 292
```

### 3. Training Configuration
```python
Hyperparameters:
- Learning rate: 0.0005
- Optimizer: Adam
- Loss function: Mean Squared Error (MSE)
- Metrics: Mean Absolute Error (MAE)
- Batch size: Default
- Epochs: 50 (with early stopping)
- Validation split: 20%

Callbacks:
1. Early Stopping:
   - Monitor: 'val_loss'
   - Patience: 15
   - Mode: 'min'

2. ReduceLROnPlateau:
   - Monitor: 'val_loss'
   - Factor: 0.1
   - Patience: 5
   - Min_lr: 0.00001
```

### 4. Training Results
```python
Training Summary:
- Best epoch: 10
- Best validation loss: 0.0060
- Final training loss: 0.1356
- Learning rate reductions: 2 times

Model Performance Metrics:
- Root Mean Square Error (RMSE): Measures average prediction error
- Mean Absolute Error (MAE): Average absolute difference between predictions and actual values
- R-squared Score (R²): Indicates how well the model fits the data
```

### 5. Implementation Details

#### Data Pipeline
```python
1. Data Loading:
   - Used yfinance to download AAPL stock data
   - Date range: 2017-01-03 to 2023-12-29
   - Daily price data with OHLCV

2. Feature Engineering:
   - Created 10 technical indicators
   - Normalized features using MinMaxScaler
   - Created sequences of 60 timesteps

3. Data Split:
   - Training: 1320 sequences (80%)
   - Testing: 331 sequences (20%)
```

#### Model Improvements
```python
1. Regularization Techniques:
   - Batch Normalization: Added after Conv1D and Dense layers
   - Dropout (0.2): Prevents overfitting
   - Early Stopping: Prevents overtraining

2. Architecture Optimization:
   - Two CNN blocks for hierarchical feature extraction
   - Reduced learning rate for stability
   - Added batch normalization for better training

3. Performance Monitoring:
   - Loss and MAE tracking
   - Learning rate adaptation
   - Validation performance monitoring
```

## Key Contributions

1. **Advanced Model Implementation**
   - Successfully implemented a CNN model for time series prediction
   - Added modern deep learning techniques (batch normalization, dropout)
   - Achieved stable training with learning rate adaptation

2. **Feature Engineering**
   - Developed comprehensive technical indicators
   - Created effective sequence-based training data
   - Implemented proper data normalization

3. **Training Optimization**
   - Implemented early stopping to prevent overfitting
   - Added learning rate reduction on plateau
   - Monitored and visualized training progress

4. **Results Analysis**
   - Tracked multiple performance metrics
   - Visualized predictions vs actual values
   - Monitored training and validation metrics 