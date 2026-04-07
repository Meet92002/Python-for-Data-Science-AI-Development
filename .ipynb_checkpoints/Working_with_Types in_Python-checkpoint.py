{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6395d2a7-e82d-4b7c-935c-f42e1714ee59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Python!\n",
      "3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]\n",
      "Hello, Python!\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'frint' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 21\u001b[39m\n\u001b[32m     18\u001b[39m \u001b[38;5;66;03m# 3. Errors in Python\u001b[39;00m\n\u001b[32m     20\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m'\u001b[39m\u001b[33mHello, Python!\u001b[39m\u001b[33m'\u001b[39m)\n\u001b[32m---> \u001b[39m\u001b[32m21\u001b[39m \u001b[43mfrint\u001b[49m(\u001b[33m\"\u001b[39m\u001b[33mHello, Python!\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[31mNameError\u001b[39m: name 'frint' is not defined"
     ]
    }
   ],
   "source": [
    "# File of Contents\n",
    "\n",
    "# 'Hello' to the world in Python\n",
    "# What version of Python are we using?\n",
    "# Writing comments in Python\n",
    "# Errors in Python\n",
    "# Does Python know about your error before it runs your code?\n",
    "# Exercise: Your First Program\n",
    "\n",
    "# 1. Say 'Hello' to the world in Python\n",
    "print('Hello, Python!')\n",
    "\n",
    "# 2. What version of Python are we using?\n",
    "\n",
    "import sys\n",
    "print(sys.version)\n",
    "\n",
    "# 3. Practice on writing comments\n",
    "\n",
    "print('Hello, Python!') # This line prints a string\n",
    "# print(\"Hi\")\n",
    "\n",
    "\n",
    "# 4. Errors in Python\n",
    "\n",
    "print('Hello, Python!')\n",
    "frint(\"Hello, Python!\")\n",
    " # Try to see built-in error message\n",
    "print(\"Hello, Python!)\n",
    "\n",
    "# 5. Python know about your error before it runs your code\n",
    "\n",
    "# Print string and error to see the running order\n",
    "\n",
    "print(\"This will be printed\")\n",
    "frint(\"This will cause an error\")\n",
    "print(\"This will NOT be printed\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f634fa0-6957-4acd-8c21-f639426bf960",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
