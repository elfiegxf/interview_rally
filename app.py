from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start', methods=["POST", "GET"])
def start():
    if request.method == 'GET':
        return render_template("start.html")
    sequence = request.form.get("sequence").strip()
    target = request.form.get("target").strip()
    if is_number(sequence) and is_number(target):
        result = compute(sequence, target)
    else:
        result = "Please type in only digits in the blanks and resubmit! \n"
    return render_template("start.html", result = result, sum = target, sequence = sequence)


def is_number(n):
    try:
        int(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`,
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def compute(sequence, target):
    list = []
    result = ""
    ans =  helper(sequence, 0, int(target), 0, 0, "", list)
    if(len(ans) == 0) :
        result = "impossible"
    else:
        for i in range(0, len(ans)):
            result = result + str(list[i]) + "\n"
    return result


def helper(digits, index, N, sum, cur, s, list):
    if (index >= len(digits)):
        if sum == N:
            list.append(s)
        return list

    for i in range(index, len(digits)):
        temp = int(digits[index: i + 1])
        if int(digits[index]) == 0 and i != index:
            break
        if index == 0:
            helper(digits, i + 1, N, temp, temp, str(temp), list)
        else:
            helper(digits, i + 1, N, sum + temp, temp, s + "+" + str(temp), list)
            helper(digits, i + 1, N, sum - temp, -temp, s + "-" + str(temp), list)
            helper(digits, i + 1, N, sum - cur + cur * temp, cur * temp, s + "*" + str(temp), list)
    return list

if __name__ == '__main__':
    app.run()
