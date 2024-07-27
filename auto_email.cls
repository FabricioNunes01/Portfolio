VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "auto_email"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub EnviarEmailParaTodasLinhas()

    Dim OutApp As Object
    Dim OutMail As Object
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long
    Dim strEmailTo As String
    Dim strCC As String
    Dim strSubject As String
    Dim strBody As String
    Dim strNome As String
    Dim strNome2 As String
    Dim strCNPJ As String
    Dim novoCNPJ As String
    Dim signature As String
    
    ' Esse programa automatiza o envio de e-mail para varias pessoas com base nas variaveis no excel
    
    ' Definir a planilha onde os dados estão localizados (Planilha2)
    Set ws = ThisWorkbook.Sheets("Planilha2")
    
    ' Última linha com dados na coluna A
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    
    ' Loop pelas linhas da planilha (começa da linha 2)
    For i = 2 To lastRow
        ' Verifica se o valor da coluna F é diferente de 0
        If ws.Cells(i, "F").Value <> 0 Then
        
            ' Valor para substituir "ZZZ" (celula H2 da Planilha2)
            strNome = ws.Cells(i, "H").Value

            ' Valor para substituir "YYY" (celula G2 da Planilha2)
            strNome2 = ws.Cells(i, "G").Value
            
            ' Valor para substituir "XXX" (celula C2 da Planilha2)
            strCNPJ = ws.Cells(i, "C").Value
            
            ' Substituir os dois últimos dígitos do CNPJ por "XX"
            novoCNPJ = Left(strCNPJ, Len(strCNPJ) - 2) & "XX"
            
            ' Endereço de e-mail para onde será enviado (celula F da linha atual)
            strEmailTo = ws.Cells(i, "F").Value
            
            ' Endereço de e-mail para cópia (Cc)
            strCC = "digital@reis.adv.br"
            
            ' Assunto do e-mail
            strSubject = ws.Cells(i, "B").Value & " | " & _
                         "Nome" & " | " & _
                         "Valor necessario: " & ws.Cells(i, "D").Value
            
            ' Corpo do e-mail em HTML com formatação apropriada
            strBody = "<html><body style='font-family: Trebuchet MS; font-size: 11 px;'>" & _
                      "<p>Aqui um teste para enviar e-mail. " & strNome & ", bom dia!</p>" & _
                      "<p>Meu nome é " & strNome2 & " e falo em nome de X.</p>" & _
                      "<p>Atenciosamente,"
            
            ' Cria uma instância do Outlook
            Set OutApp = CreateObject("Outlook.Application")
            Set OutMail = OutApp.CreateItem(0)  ' 0 = E-mail
            
            ' Exibe o e-mail antes de adicionar a assinatura (opcional)
            With OutMail
                .Display  ' Abre o e-mail para revisão (opcional)
            End With
            
            ' Captura a assinatura HTML
            signature = OutMail.HTMLBody
            
            ' Atualiza o e-mail com a assinatura
            With OutMail
                .To = strEmailTo
                .CC = strCC
                .Subject = strSubject
                .HTMLBody = strBody & "<br><br>" & signature  ' Adiciona a assinatura ao final
                .Display  ' Abre o e-mail para revisão (opcional)
                '.Send
            End With
            
            ' Limpa a memória
            Set OutMail = Nothing
            Set OutApp = Nothing
        
        End If
    Next i

End Sub



