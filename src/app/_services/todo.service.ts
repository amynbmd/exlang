import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { Todos } from '../home/home.component';
import { ConfigService } from '../_shared/config/config.service';

@Injectable({
  providedIn: 'root',
})
export class TodoService {
  private readonly baseUrl = this._configService.config?.apiUrl + 'todos/';

  private readonly httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  constructor(
    private _http: HttpClient,
    private _configService: ConfigService
  ) {}

  postTodo(todos: Todos): Observable<any> {
    return this._http
      .post<Todos>(this.baseUrl + 'bulk', todos, this.httpOptions)
      .pipe(
        map((res) => {
          return res;
        })
      );
  }
}
