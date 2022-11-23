//Default Modules
import { APP_INITIALIZER, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

//Custom Modules

//Custom Services

//Components
import { AppComponent } from './app.component';
import { StyleManager } from './layout/data-access/style-manager/style-manager';
import { ConfigService } from './_shared/config/config.service';
import { CookieModule } from 'ngx-cookie';
import { AuthenticationInterceptor } from './account/_services/authentication/authentication.intercepter';
import { JwtModule } from '@auth0/angular-jwt';
import { LayoutModule } from './layout/layout.module';
import { EffectsModule } from '@ngrx/effects';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { environment } from '../environments/environment';
import { StoreModule } from '@ngrx/store';
import { ThemeStorage } from './layout/ui/theme-picker/theme-storage/theme-storage';


export function getAppConfig(configService: ConfigService) {
  return () => configService.loadConfiguration();
}

@NgModule({
  declarations: [		AppComponent
   ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    StoreModule.forRoot({}),
    CookieModule.withOptions(),
    JwtModule.forRoot({
      config: {
        tokenGetter: () => localStorage.getItem('jwt'),
      },
    }),
    LayoutModule,
    EffectsModule.forRoot(),
    StoreDevtoolsModule.instrument({
      maxAge: 25, // Retains last 25 states
      logOnly: environment.production, // Restrict extension to log-only mode
      autoPause: true, // Pauses recording actions and state changes when the extension window is not open
    }),
  ],
  providers: [
    ConfigService,
    {
      provide: APP_INITIALIZER,
      useFactory: getAppConfig,
      deps: [ConfigService],
      multi: true,
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthenticationInterceptor,
      multi: true,
    },
    StyleManager,
    ThemeStorage,
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
