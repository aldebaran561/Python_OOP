{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Car:\n",
    "    \n",
    "    def accelerate(self):\n",
    "        return 'This car is on moving'\n",
    "\n",
    "class Gas(Car):\n",
    "    def accelerate(self):\n",
    "        return 'This Car moves on gas'\n",
    "\n",
    "class Electric(Car):\n",
    "    def accelerate(self):\n",
    "        return 'This Car moves on electric' "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This car is on moving\n",
      "This Car moves on gas\n",
      "This Car moves on electric\n"
     ]
    }
   ],
   "source": [
    "ferrari = Car()\n",
    "print(ferrari.accelerate())\n",
    "\n",
    "bus = Gas()\n",
    "print(bus.accelerate())\n",
    "\n",
    "tesla = Electric()\n",
    "print(tesla.accelerate())"
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
