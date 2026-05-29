import math
from flask import render_template, request

def calcular():
    
    num1_valor = request.form.get("num1", "").strip()
    operacao = request.form.get("operacao", "")

    
    if not num1_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o primeiro número.",
            resultados="",
        )

    num1 = float(num1_valor)

   
    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Não existe raiz quadrada real de {num1}. Número deve ser positivo."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"


    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro"
            etapas = f"Não existe logaritmo de {num1}. Número deve ser maior que zero."
        else:
            resultado = math.log10(num1)
            etapas = f"log₁₀({num1}) = {resultado}"

   
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )

        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"

        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2} = {resultado}"

        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro"
                etapas = f"Divisão por zero não é permitida. ({num1} ÷ 0)"
            else:
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"

        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado}"

        else:
            resultado = "Erro"
            etapas = "Operação inválida."

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado,
    )