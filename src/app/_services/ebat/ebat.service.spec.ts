/* tslint:disable:no-unused-variable */

import { HttpClientTestingModule } from '@angular/common/http/testing';
import { TestBed, async, inject } from '@angular/core/testing';
import { EbatService } from './ebat.service';

describe('Service: Ebat', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule], 
      providers: [EbatService]
    });
  });

  it('should ...', inject([EbatService], (service: EbatService) => {
    expect(service).toBeTruthy();
  }));
});
