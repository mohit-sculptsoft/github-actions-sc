import React, { Suspense } from "react";
import ReactDOM from "react-dom";
import "@intelliante/intelliante-ui/src/assets/scss/main.scss";
import { Loader } from "@intelliante/intelliante-ui";


import "assets/scss/main.scss";

import "config/languageConfig/i18next";

import TypingContextContainer from "contextAPI/TypingContextContainer";
import { UserAuthContextProvider } from "contextAPI/UserAuthContext";

import App from "containers/App";

import { THEME } from "constants/localStorageKey";

import PreloadAssets from "pages/PreloadAssets";

import LocalStorageManager from "lib/localStorageManger";


ReactDOM.render(
  <React.StrictMode>
    <Suspense
      fallback={<Loader theme={LocalStorageManager.getItem(THEME.KEY)} />}
    >
      <UserAuthContextProvider>
        <PreloadAssets>
        <TypingContextContainer>
          <App />
        </TypingContextContainer>
        </PreloadAssets>
      </UserAuthContextProvider>
    </Suspense>
  </React.StrictMode>,
  document.getElementById("root")
);
