{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ff53d2a1-a8cb-4f2d-87ea-90495eb2b526",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Options:\n",
      "1. Display to-do list\n",
      "2. Add a task\n",
      "3. Mark a task as completed\n",
      "4. Remove a task\n",
      "5. Quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your to-do list is empty.\n",
      "\n",
      "Options:\n",
      "1. Display to-do list\n",
      "2. Add a task\n",
      "3. Mark a task as completed\n",
      "4. Remove a task\n",
      "5. Quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n",
      "Enter the task:  working on Task One\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Task 'working on Task One' added to your to-do list.\n",
      "\n",
      "Options:\n",
      "1. Display to-do list\n",
      "2. Add a task\n",
      "3. Mark a task as completed\n",
      "4. Remove a task\n",
      "5. Quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "To-Do List:\n",
      "1. working on Task One (Not Done)\n",
      "\n",
      "Options:\n",
      "1. Display to-do list\n",
      "2. Add a task\n",
      "3. Mark a task as completed\n",
      "4. Remove a task\n",
      "5. Quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "To-Do List:\n",
      "1. working on Task One (Not Done)\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the task number to remove:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Task 'working on Task One' removed from your to-do list.\n",
      "\n",
      "Options:\n",
      "1. Display to-do list\n",
      "2. Add a task\n",
      "3. Mark a task as completed\n",
      "4. Remove a task\n",
      "5. Quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  5\n"
     ]
    }
   ],
   "source": [
    "# Define an empty list to store tasks\n",
    "tasks = []\n",
    "\n",
    "# Function to display the to-do list\n",
    "def display_tasks():\n",
    "    if not tasks:\n",
    "        print(\"Your to-do list is empty.\")\n",
    "    else:\n",
    "        print(\"To-Do List:\")\n",
    "        for i, task in enumerate(tasks, start=1):\n",
    "            status = \"Done\" if task[\"completed\"] else \"Not Done\"\n",
    "            print(f\"{i}. {task['task']} ({status})\")\n",
    "\n",
    "# Function to add a task to the to-do list\n",
    "def add_task(task_name):\n",
    "    task = {\"task\": task_name, \"completed\": False}\n",
    "    tasks.append(task)\n",
    "    print(f\"Task '{task_name}' added to your to-do list.\")\n",
    "\n",
    "# Function to mark a task as completed\n",
    "def mark_completed(task_number):\n",
    "    if 1 <= task_number <= len(tasks):\n",
    "        tasks[task_number - 1][\"completed\"] = True\n",
    "        print(f\"Task {task_number} marked as completed.\")\n",
    "    else:\n",
    "        print(\"Invalid task number. Please enter a valid task number.\")\n",
    "\n",
    "# Function to remove a task from the to-do list\n",
    "def remove_task(task_number):\n",
    "    if 1 <= task_number <= len(tasks):\n",
    "        removed_task = tasks.pop(task_number - 1)\n",
    "        print(f\"Task '{removed_task['task']}' removed from your to-do list.\")\n",
    "    else:\n",
    "        print(\"Invalid task number. Please enter a valid task number.\")\n",
    "\n",
    "# Main program loop\n",
    "while True:\n",
    "    print(\"\\nOptions:\")\n",
    "    print(\"1. Display to-do list\")\n",
    "    print(\"2. Add a task\")\n",
    "    print(\"3. Mark a task as completed\")\n",
    "    print(\"4. Remove a task\")\n",
    "    print(\"5. Quit\")\n",
    "    choice = input(\"Enter your choice: \")\n",
    "\n",
    "    if choice == '1':\n",
    "        display_tasks()\n",
    "    elif choice == '2':\n",
    "        task_name = input(\"Enter the task: \")\n",
    "        add_task(task_name)\n",
    "    elif choice == '3':\n",
    "        display_tasks()\n",
    "        task_number = int(input(\"Enter the task number to mark as completed: \"))\n",
    "        mark_completed(task_number)\n",
    "    elif choice == '4':\n",
    "        display_tasks()\n",
    "        task_number = int(input(\"Enter the task number to remove: \"))\n",
    "        remove_task(task_number)\n",
    "    elif choice == '5':\n",
    "        break\n",
    "    else:\n",
    "        print(\"Invalid choice. Please enter a valid option.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8db60df9-ce87-4aa4-8d56-aae12552fad0",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
