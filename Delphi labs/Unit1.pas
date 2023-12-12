unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Label2: TLabel;
    Edit1: TEdit;
    Edit2: TEdit;
    RadioButton1: TRadioButton;
    RadioButton2: TRadioButton;
    RadioButton3: TRadioButton;
    RadioButton4: TRadioButton;
    Button1: TButton;
    Edit3: TEdit;
    procedure Button1Click(Sender: TObject);
    procedure RadioButton1Click(Sender: TObject);
    procedure RadioButton3Click(Sender: TObject);
    procedure RadioButton4Click(Sender: TObject);
    procedure RadioButton2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
begin
randomize;
Edit1.text := IntToStr(random(10));
Edit2.text := IntToStr(random(10));



end;

procedure TForm1.RadioButton1Click(Sender: TObject);
var a: Integer;
begin
a :=  StrToInt(Edit1.Text)  + StrToInt(Edit2.Text);

Edit3.Text :=  IntToStr(a)

end;

procedure TForm1.RadioButton2Click(Sender: TObject);
var a: real;
begin
a :=  StrToFloat(Edit1.Text) / StrToFloat(Edit2.Text);

Edit3.Text :=  FloatToStr(a)
end;

procedure TForm1.RadioButton3Click(Sender: TObject);
var a: Integer;
begin
a :=  StrToInt(Edit1.Text) - StrToInt(Edit2.Text);

Edit3.Text := IntToStr(a)
end;

procedure TForm1.RadioButton4Click(Sender: TObject);
var a: integer;
begin
a :=  StrToInt(Edit1.Text) * StrToInt(Edit2.Text);

Edit3.Text :=  IntToStr(a)
end;

end.
