; PDF Extractor Pro - Inno Setup Script
; Creates a Windows installer (.exe) for the application

#define MyAppName "PDF Extractor Pro"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "PDF Extractor"
#define MyAppURL "https://github.com/ione2025/PDF-Extractor"
#define MyAppExeName "PDF_Extractor_Pro.exe"

[Setup]
; Application Information
AppId={{8F9A2D3E-5B1C-4A7E-9D8F-2C3E4A5B6C7D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}

; Installation Directories
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes

; Output Configuration
OutputDir=installer
OutputBaseFilename=PDF_Extractor_Pro_Setup
SetupIconFile=compiler:SetupClassicIcon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

; Privileges
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog

; Architecture
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Copy all files from the PyInstaller dist folder
Source: "dist\PDF_Extractor_Pro\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Start Menu shortcut
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

; Desktop shortcut (if task selected)
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Option to run the application after installation
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
// Custom installation messages
function InitializeSetup(): Boolean;
begin
  Result := True;
  MsgBox('Welcome to PDF Extractor Pro Setup!' + #13#10 + #13#10 + 
         'This will install the application on your computer.' + #13#10 + 
         'The app includes:' + #13#10 + 
         '  • PDF Text Extraction with Multi-language OCR' + #13#10 + 
         '  • AI-Powered Image Analysis' + #13#10 + 
         '  • Excel Report Generation' + #13#10 + #13#10 + 
         'Click Next to continue.', 
         mbInformation, MB_OK);
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    MsgBox('Installation Complete!' + #13#10 + #13#10 + 
           'PDF Extractor Pro has been installed successfully.' + #13#10 + #13#10 + 
           'The application will open in your default web browser.' + #13#10 + 
           'You can access it at: http://localhost:5000' + #13#10 + #13#10 + 
           'Note: Ensure Tesseract OCR and Poppler are installed for full functionality.',
           mbInformation, MB_OK);
  end;
end;
