/* tslint:disable:no-unused-variable */

import { HttpClientTestingModule } from '@angular/common/http/testing';
import { TestBed, async, inject } from '@angular/core/testing';
import { TodoService } from './todo.service';

describe('Service: Todo', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [TodoService]
    });
  });

  it('should ...', inject([TodoService], (service: TodoService) => {
    expect(service).toBeTruthy();
  }));
});
