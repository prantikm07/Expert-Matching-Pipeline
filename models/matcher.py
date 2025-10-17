import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import pickle
import os
from pathlib import Path

warnings.filterwarnings('ignore')

class MentorMenteeMatchingSystem:
    """Production-ready mentor-mentee matching system with caching and real-time support"""
    
    def __init__(self, model_name='all-MiniLM-L6-v2', cache_dir='models/embeddings'):
        """
        Initialize the matching system
        
        Args:
            model_name: Sentence transformer model name
            cache_dir: Directory to cache embeddings
        """
        print(f"Loading sentence transformer model: {model_name}...")
        self.model = SentenceTransformer(model_name)
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        self.mentors_df = None
        self.mentor_embeddings = None
        self.embeddings_cached = False
        
    def load_mentors(self, csv_path, use_cache=True):
        """
        Load mentor data from CSV with optional embedding caching
        
        Args:
            csv_path: Path to mentors CSV file
            use_cache: Whether to use cached embeddings
        """
        try:
            self.mentors_df = pd.read_csv(csv_path)
            print(f"✓ Loaded {len(self.mentors_df)} mentors from {csv_path}")
            
            # Validate required columns
            required_columns = ['mentor_name', 'mentor_description']
            for col in required_columns:
                if col not in self.mentors_df.columns:
                    raise ValueError(f"Missing required column: {col}")
            
            # Try loading cached embeddings
            cache_file = self.cache_dir / f"{Path(csv_path).stem}_embeddings.pkl"
            
            if 
