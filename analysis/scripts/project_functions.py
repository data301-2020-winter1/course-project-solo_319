{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(path):\n",
    "    \n",
    "    # Method Chain 1 (for cleaning data and dropping columns):\n",
    "    \n",
    "    df = (   \n",
    "    pd.read_csv(path)\n",
    "    .drop(['case', 'cc3', 'gdp_weighted_default', 'independence', 'currency_crises', 'inflation_crises', 'banking_crisis'], axis=1)\n",
    "    .dropna()\n",
    "    .reset_index(drop=True)\n",
    "    )\n",
    "    \n",
    "    # Method Chain 2 (for dropping rows and resetting index):\n",
    "    \n",
    "    df1 = (\n",
    "    df[df.year >= 2000]\n",
    "    .reset_index(drop=True)\n",
    "    )\n",
    "    \n",
    "    return df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
