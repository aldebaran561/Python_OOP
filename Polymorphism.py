{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Parrot can fly\n",
      "Penguin can't fly\n"
     ]
    }
   ],
   "source": [
    "class Parrot:\n",
    "\n",
    "    def fly(self):\n",
    "        print(\"Parrot can fly\")\n",
    "    \n",
    "    def swim(self):\n",
    "        print(\"Parrot can't swim\")\n",
    "\n",
    "class Penguin:\n",
    "\n",
    "    def fly(self):\n",
    "        print(\"Penguin can't fly\")\n",
    "    \n",
    "    def swim(self):\n",
    "        print(\"Penguin can swim\")\n",
    "\n",
    "# common interface\n",
    "def flying_test(bird):\n",
    "    bird.fly()\n",
    "\n",
    "#instantiate objects\n",
    "blu = Parrot()\n",
    "peggy = Penguin()\n",
    "\n",
    "# passing the object\n",
    "flying_test(blu)\n",
    "flying_test(peggy)"
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
