unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.ExtCtrls;

type
  TForm1 = class(TForm)
    Image1: TImage;
    procedure FormActivate(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.FormActivate(Sender: TObject);
begin
Image1.Canvas.Rectangle(60,100,400,300);
Image1.Canvas.MoveTo(60,100);
Image1.Canvas.LineTo(245,5);
Image1.Canvas.LineTo(400,100);
Image1.Canvas.Ellipse(300,150,150,250);
Image1.Canvas.MoveTo(150,200);
Image1.Canvas.LineTo(300,200);
Image1.Canvas.MoveTo(230,200);
Image1.Canvas.LineTo(230,250);
Image1.Canvas.LineTo(230,150);

end;


end.
