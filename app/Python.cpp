/* Copyright (c) 2005 Nokia Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
//
// Python.cpp
//
// Implementation of a minimal application
// that has the role of a launchpad for Python applications.
// The common parts that comprise the S60 adaptation layer of the
// S60 Python have been collected into a separate DLL.
// 

#include "Python_app.h"
#include <Python.rsg>

IMPORT_C CEikAppUi* CreateAmarettoAppUi(TInt);

const TUid KUidPythonApp = {0x10201510};

CPythonDocument::CPythonDocument(CEikApplication& aApp) : CAknDocument(aApp) 
{
}

CEikAppUi* CPythonDocument::CreateAppUiL() 
{
  CEikAppUi* appui = CreateAmarettoAppUi(R_PYTHON_EXTENSION_MENU);
  if (!appui)
    User::Leave(KErrNoMemory);
  return appui;
}

TUid CPythonApplication::AppDllUid() const 
{
  return KUidPythonApp;
}

CApaDocument* CPythonApplication::CreateDocumentL() 
{
  return new (ELeave) CPythonDocument(*this);
}

EXPORT_C CApaApplication* NewApplication() 
{
  return new CPythonApplication;
}

GLDEF_C TInt E32Dll(TDllReason) 
{
  return KErrNone;
}
