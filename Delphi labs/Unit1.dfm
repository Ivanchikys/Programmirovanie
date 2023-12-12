object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Calculator PI'
  ClientHeight = 361
  ClientWidth = 628
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  TextHeight = 15
  object Label1: TLabel
    Left = 28
    Top = 48
    Width = 78
    Height = 15
    Caption = #1055#1077#1088#1074#1086#1077' '#1095#1080#1089#1083#1086
  end
  object Label2: TLabel
    Left = 20
    Top = 101
    Width = 76
    Height = 15
    Caption = #1042#1090#1086#1088#1086#1077' '#1095#1080#1089#1083#1086
  end
  object Edit1: TEdit
    Left = 112
    Top = 45
    Width = 121
    Height = 23
    TabOrder = 0
  end
  object Edit2: TEdit
    Left = 112
    Top = 98
    Width = 121
    Height = 23
    TabOrder = 1
  end
  object RadioButton1: TRadioButton
    Left = 300
    Top = 48
    Width = 113
    Height = 17
    Caption = #1057#1083#1086#1078#1077#1085#1080#1077
    TabOrder = 2
    OnClick = RadioButton1Click
  end
  object RadioButton2: TRadioButton
    Left = 439
    Top = 101
    Width = 113
    Height = 17
    Caption = #1044#1077#1083#1077#1085#1080#1077
    TabOrder = 3
    OnClick = RadioButton2Click
  end
  object RadioButton3: TRadioButton
    Left = 300
    Top = 101
    Width = 113
    Height = 17
    Caption = #1042#1099#1095#1080#1090#1072#1085#1080#1077
    TabOrder = 4
    OnClick = RadioButton3Click
  end
  object RadioButton4: TRadioButton
    Left = 439
    Top = 48
    Width = 113
    Height = 17
    Caption = #1059#1084#1085#1086#1078#1077#1085#1080#1077
    TabOrder = 5
    OnClick = RadioButton4Click
  end
  object Button1: TButton
    Left = 344
    Top = 240
    Width = 233
    Height = 65
    Caption = #1057#1092#1086#1088#1084#1080#1088#1086#1074#1072#1090#1100' '#1095#1080#1089#1083#1072
    TabOrder = 6
    OnClick = Button1Click
  end
  object Edit3: TEdit
    Left = 20
    Top = 224
    Width = 225
    Height = 95
    ReadOnly = True
    TabOrder = 7
  end
end
