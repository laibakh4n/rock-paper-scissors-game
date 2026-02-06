# ===========================================================================
#                                    ROCK PAPER SCISSOR GAME
# # ==========================================================================
import random
import tkinter as tk
from tkinter import messagebox
import winsound

# Game setup
options = ["Rock", "Paper", "Scissors"]
computer_score = 0
player_score = 0
tie_count = 0
player_streak = 0
best_streak = 0

# Milestones
MILESTONES = [5, 10]

# Dark theme colors
BG_COLOR = "#121212"
CARD_COLOR = "#1e1e1e"
ACCENT = "#00c2ff"
TEXT_COLOR = "#f5f5f5"
STREAK_COLOR = "#ffcc00"
GLOW_COLOR = "#00ff99"


def play_sound(result):
    if result == "YOU WIN":
        winsound.Beep(1200, 200)
        winsound.Beep(1500, 200)
    elif result == "Computer WIN":
        winsound.Beep(400, 300)
    else:
        winsound.Beep(800, 150)


def play_milestone_sound():
    winsound.Beep(1600, 150)
    winsound.Beep(1800, 150)
    winsound.Beep(2000, 200)


def save_result(player, computer, result):
    with open("game_scores.txt", "a") as file:
        file.write(
            f"\nPlayer: {player}, Computer: {computer}, Result: {result}, "
            f"Score = You: {player_score}, Computer: {computer_score}, "
            f"Ties: {tie_count}, Streak: {player_streak}\n"
        )


def animate_score():
    score_label.config(
        text=(
            f"Player: {player_score}   Computer: {computer_score}   Ties: {tie_count}"
        ),
        fg=ACCENT,
    )
    root.after(200, lambda: score_label.config(fg=TEXT_COLOR))


def glow_streak():
    streak_label.config(fg=GLOW_COLOR)
    root.after(400, lambda: streak_label.config(fg=TEXT_COLOR))


def animate_streak():
    streak_label.config(fg=STREAK_COLOR)
    root.after(250, lambda: streak_label.config(fg=TEXT_COLOR))


def check_milestones():
    if player_streak in MILESTONES:
        play_milestone_sound()
        glow_streak()
        messagebox.showinfo(
            "Streak Milestone!",
            f"🔥 Amazing! You reached a {player_streak} win streak!",
        )


def update_streak(win):
    global player_streak, best_streak

    if win:
        player_streak += 1

        if player_streak > best_streak:
            best_streak = player_streak
            messagebox.showinfo(
                "New Record!",
                f"🏆 New best streak: {best_streak}!",
            )

        check_milestones()

    else:
        player_streak = 0

    streak_label.config(
        text=f"🔥 Streak: {player_streak}   Best: {best_streak}"
    )
    animate_streak()


def play(player_choice):
    global computer_score, player_score, tie_count

    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        tie_count += 1
        result_text = "It's a Tie!"
        result = "TIE"
        update_streak(False)

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        player_score += 1
        result_text = "You Win!"
        result = "YOU WIN"
        update_streak(True)

    else:
        computer_score += 1
        result_text = "Computer Wins!"
        result = "Computer WIN"
        update_streak(False)

    play_sound(result)
    save_result(player_choice, computer_choice, result)

    result_label.config(
        text=(
            f"You chose: {player_choice}\n"
            f"Computer chose: {computer_choice}\n"
            f"{result_text}"
        )
    )

    animate_score()


def end_game():
    summary = (
        f"Final Scores:\n"
        f"Player: {player_score}\n"
        f"Computer: {computer_score}\n"
        f"Ties: {tie_count}\n"
        f"Best Streak: {best_streak}"
    )

    with open("game_scores.txt", "a") as file:
        file.write(
            f"\n--- GAME ENDED ---\n"
            f"Final Score You: {player_score}, Computer: {computer_score}, "
            f"Ties: {tie_count}, Best Streak: {best_streak}\n\n"
        )

    messagebox.showinfo("Game Over", summary)
    root.destroy()


# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("460x380")
root.configure(bg=BG_COLOR)


title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 16, "bold"),
    bg=BG_COLOR,
    fg=ACCENT,
)
title_label.pack(pady=10)


button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)


for choice in options:
    btn = tk.Button(
        button_frame,
        text=choice,
        width=10,
        bg=CARD_COLOR,
        fg=TEXT_COLOR,
        activebackground=ACCENT,
        activeforeground="black",
        relief="flat",
        command=lambda c=choice: play(c),
    )
    btn.pack(side=tk.LEFT, padx=6)


result_label = tk.Label(
    root,
    text="Make your move!",
    font=("Arial", 11),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
result_label.pack(pady=12)


score_label = tk.Label(
    root,
    text="Player: 0   Computer: 0   Ties: 0",
    font=("Arial", 10, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
score_label.pack(pady=5)


streak_label = tk.Label(
    root,
    text="🔥 Streak: 0   Best: 0",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
streak_label.pack(pady=6)


end_button = tk.Button(
    root,
    text="End Game",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    activebackground="#ff4d4d",
    relief="flat",
    command=end_game,
)
end_button.pack(pady=12)


root.mainloop()